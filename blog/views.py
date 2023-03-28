from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    View, ListView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.db.models import Count, Q
from .models import *
from .forms import CommentForm, PostForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


def search_posts(request):
    """
    Method for searching for posts based on the title or author name
    """
    if request.method == 'POST':
        # Getting the search query from the form data
        searched = request.POST.get('searched', '')

        # Filtering the Post model based on the title or author name
        posts = Post.objects.filter(Q(
            title__contains=searched) | Q(author__username__contains=searched))

        paginator = Paginator(posts, 5)  # Include only 5 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)    

        return render(request, 'search_posts.html', {
            'searched': searched, 'page_obj': page_obj})
    else:
        message = "Search unsuccessful"
        return render(request, 'search_posts.html', {'message': message})


class CategoryView(ListView):
    """
    Class based view for displaying posts in selected category
    """
    model = Post
    template_name = 'categories.html'
    # Name of the context variable to be used in the template
    context_object_name = 'category_posts'
    paginate_by = 5

    def get_queryset(self):
        """
        Overriding the get_queryset method to filter posts based on the
        category selected and display them in descending order
        of creation date + add comment count.
        """
        cat = self.kwargs['cat']
        return Post.objects.filter(category=cat, status=1).order_by(
            '-created_on').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        """
        Overriding the get_context_data method to add the category name
        to the context data
        """
        context = super().get_context_data(**kwargs)
        context['cat'] = self.kwargs['cat']
        return context


class CreatePostView(CreateView):
    """
    Class based view for creating new post
    """
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        """
        Overriding the form valid method to set the author of the post
        to the current logged in user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    """
    Class based view for updating existing post
    """
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def form_valid(self, form):
        """
        Overriding the form valid method to set the author of the post
        to the current logged in user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def update_post(request, slug):
        """
        Method for update the post and return a response
        """
        # Get the post instance from the database
        post = get_object_or_404(Post, slug=slug)
        # Check if the current user is the author of the post or staff
        if request.user != post.author and not request.user.is_staff:
            # If not return a forbidden response
            return HttpResponseForbidden()
        if request.method == 'POST':
            # Create a new form instance with the updated data
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.isvalid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect(post.get_absolute_url())
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/blog.html', {'form': form})


class DeletePostView(DeleteView):
    """
    Class based view for deleting the post
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')


class PostList(ListView):
    """
    Class based view for viewing all the posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by(
        '-created_on').annotate(comment_count=Count('comments'))
    template_name = 'blog.html'
    cat = Category.objects.all()
    paginate_by = 5


class PostLike(View):
    """
    Add or remove like for a post
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect((reverse('post_detail', args=[slug])))


class PostDetail(View):
    """
    Class based view of a blog post with all the details
    """
    def get(self, request, slug, *args, **kwargs):
        # Filters the published blog posts and count num of comments
        queryset = Post.objects.filter(
            status=1).annotate(comment_count=Count('comments'))
        # Retrieves a post with given slug or raises 404 err if doesnt exist
        post = get_object_or_404(queryset, slug=slug)
        # Retrieves the approved comments for the post
        comments = post.comments.filter(approved=True)
        # Check if logged in user has liked the post or not
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # renders the post detail view with comments, liked status,comment form
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(
            status=1).annotate(comment_count=Count('comments'))
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Creates a new comment instance and saves it to the database if valid
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            # Form with the submitted data and errors
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


@login_required
def profile_view(request):
    """
    Method for retrieve and displaying user object for
    the logged in user or raises 404 err if not existing.
    If the user is not logged in @login_required decorator
    ensures that the use is redirected to the login page.
    """
    user = get_object_or_404(User, username=request.user.username)
    # retrieves blog posts of the user
    posts = Post.objects.filter(author=user)
    # provides the form with the user data to update the profile info
    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':
        # Processes te form submission to update user info
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your profile has been updated !',
                extra_tags='profile_updated')
            return HttpResponseRedirect(reverse(profile_view))
        else:
            form = UserUpdateForm(instance=request.user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Something went wrong!',
                extra_tags='profile_updated')
            return HttpResponseRedirect(reverse(profile_view))
    # create a context dictionary with the user object, posts and form
    context = {'user': user, 'posts': posts, 'form': form}
    # render the profile page with the context dictionary
    return render(request, 'profile.html', context)


def error_404_view(request, exception):
    return render(request, '404.html')


def error_403_view(request, exception):
    return render(request, '403.html')


def error_500_view(request):
    return render(request, '500.html', status=500)

from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.db.models import Count, Q
from .models import *
from .forms import CommentForm, PostForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def search_posts(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        posts = Post.objects.filter(Q(title__contains=searched) | Q(author__username__contains=searched))
        return render(request, 'search_posts.html', {'searched': searched, 'posts': posts})
    else: 
        return render(request, 'search_posts.html', {})


class CategoryView(ListView):
    model = Post
    template_name = 'categories.html'
    context_object_name = 'category_posts'
    paginate_by = 5

    def get_queryset(self):
        cat = self.kwargs['cat']
        return Post.objects.filter(category=cat, status=1).order_by('-created_on').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = self.kwargs['cat']
        return context   


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def update_post(request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.user != post.author and not request.user.is_staff:
            return HttpResponseForbidden()
        if request.method == 'POST':
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
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on').annotate(comment_count=Count('comments'))
    template_name = 'blog.html'
    cat = Category.objects.all()
    paginate_by = 5


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect((reverse('post_detail', args=[slug])))


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1).annotate(comment_count=Count('comments'))
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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
        queryset = Post.objects.filter(status=1).annotate(comment_count=Count('comments'))
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
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

    user = get_object_or_404(User, username=request.user.username)
    posts = Post.objects.filter(author=user)
    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return HttpResponseRedirect(reverse(profile_view))
        else:
            form = UserUpdateForm(instance=request.user)
    context = {'user': user, 'posts': posts, 'form': form}

    return render(request, 'profile.html', context)
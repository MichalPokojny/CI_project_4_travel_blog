from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.db.models import Count
from .models import *
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def CategoryView(request, cat):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    category_posts = Post.objects.filter(category=cat).annotate(comment_count=Count('comments'))
    return render(request, 'categories.html', {'cat': cat, 'category_posts': category_posts})


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
    context = {'user': user, 'posts': posts}
    return render(request, 'profile.html', context)
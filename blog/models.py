from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Model for blog post
    """
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    comment_count = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=22, decimal_places=6, default=0)
    longtitute = models.DecimalField(max_digits=22, decimal_places=6, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        # return reverse('post_detail', args=[self.slug]) 
        return reverse('blog') 


class Comment(models.Model):
    """
    Model for comments in post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


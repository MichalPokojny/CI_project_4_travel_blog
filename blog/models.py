from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
    """
    Model for Post categories
    """
    title = models.CharField(max_length=30)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Model for blog post
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    comment_count = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longtitute = models.DecimalField(max_digits=22, decimal_places=16)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments on post
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
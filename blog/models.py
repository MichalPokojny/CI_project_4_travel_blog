from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.urls import reverse

# Tuple of choices for the status field of Post model
STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
    """
    Model for blog post category
    """
    name = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the absolute url for the blog page
        """
        return reverse('blog')


class Post(models.Model):
    """
    Model for blog post
    """
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    category = models.CharField(max_length=255, default='Travel')
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:

        ordering = ['-created_on']  # Ordering posts by created date

    def __str__(self):
        """
        Returns the string representation of the post object
        """
        return str(self.author) + ' | ' + self.title

    def number_of_likes(self):
        """
        Returns the number of likes for the post
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate slug from the title and save
        the post.
        """
        self.slug = slugify(self.title.replace(' ', '-'))
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the absolute url for the blog page
        """
        return reverse('blog')


class Comment(models.Model):
    """
    Model for comments in post
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_comment')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']  # Ordering comments by created date

    def __str__(self):
        """
        Returns the string representation of the comment object
        """
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    """
    Model for User profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation profile object
        """
        return f'{self.user.username} Profile'

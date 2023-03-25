from .models import Comment, Post, Category, User
from django import forms
from django_summernote.widgets import SummernoteWidget

# Get all categories from the database and store them in the list of tuples
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

# Iterate over each category and append it to the choice list
for item in choices:
    choice_list.append(item)


class CommentForm(forms.ModelForm):
    """
    Form to submit a comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    A form to create or update post
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'category',
            'excerpt',
            'content',
            'status',)

        # Define the widgets used for fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}),
            'category': forms.Select(
                choices=choice_list, attrs={'class': 'form-select'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        # Override default constructor, add custom attributes to the fields

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['featured_image'].widget.attrs.update(
                {'accept': 'image/*'})
            self.fields['featured_image'].widget.attrs.update(
                {'enctype': 'multipart/form-data'})


class UserUpdateForm(forms.ModelForm):
    """
    A form to update users acc information
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

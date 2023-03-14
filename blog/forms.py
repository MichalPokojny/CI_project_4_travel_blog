from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'excerpt', 'content', 'status', 'latitude', 'longtitute')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': SummernoteWidget(attrs={'class': 'form-control'}), 
            'status': forms.Select(attrs={'class': 'form-select'}), 
            'latitude': forms.NumberInput(attrs={'class': 'form-control',}), 
            'longtitute': forms.NumberInput(attrs={'class': 'form-control',})
        }
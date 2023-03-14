from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'featured_image', 'excerpt', 'content', 'status', 'latitude', 'longtitute')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}), 
            'featured_image': forms.TextInput(attrs={'class': 'form-control'}), 
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}), 
            
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
            'status': forms.Select(attrs={'class': 'form-select'}), 
            'latitude': forms.TextInput(attrs={'class': 'form-control'}), 
            'longtitute': forms.TextInput(attrs={'class': 'form-control'})
        }
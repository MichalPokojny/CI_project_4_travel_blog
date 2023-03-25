from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# registering the category model to the admin site
admin.site.register(Category)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Registering the Post model with the admin site
    using the SummerNoteModelAdmin
    """
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Registering the comment model to the admin site
    """

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        # method used to approve selected comments
        queryset.update(approved=True)

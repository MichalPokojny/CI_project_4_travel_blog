from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/edit/<slug:slug>', views.UpdatePostView.as_view(), name='update_post'),
    path('post/<slug:slug>/delete', views.DeletePostView.as_view(), name='delete_post'),
]
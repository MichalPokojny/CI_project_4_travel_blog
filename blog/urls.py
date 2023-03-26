from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/edit/<slug:slug>', views.UpdatePostView.as_view(
    ), name='update_post'),
    path('post/<slug:slug>/delete', views.DeletePostView.as_view(
    ), name='delete_post'),
    path('category/<str:cat>/', views.CategoryView.as_view(), name='category'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='blog_likes'),
    path('profile/', views.profile_view, name='profile_view'),
    path('search/', views.search_posts, name='search_posts'), ]

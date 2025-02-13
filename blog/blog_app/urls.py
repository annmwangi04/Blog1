from django.urls import path
from .views import (
    home, about, contact, PostListView, PostDetailView, create_post, update_post, delete_post, user_posts
)

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),
    path("about/", about, name='blog-about'),
    path("contact/", contact, name='blog-contact'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", create_post, name='create-post'),  
    path("post/update/<int:pk>/", update_post, name="update-post"),
    path("post/delete/<int:pk>/", delete_post, name="delete-post"),
    path("post/user/<int:user_id>/", user_posts, name="user-post"),  # ✅ Fixed function name
]

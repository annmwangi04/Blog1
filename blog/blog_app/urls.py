from django.urls import path
from .views import home, about, contact, PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name = 'blog-home'),
    path("about/", about, name = 'blog-about'),
    path("contact/", contact, name = 'blog-contact'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]
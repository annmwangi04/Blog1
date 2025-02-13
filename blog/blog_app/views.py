from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User  # ✅ Import User model
from .models import Post
from .forms import CreatePostForm, UpdatePostForm

# Function-based home view (Not needed if using PostListView)
def home(request):
    posts = Post.objects.all().order_by("-date_created")
    return render(request, "blog_app/home.html", {"posts": posts, "title": "Home"})

# Class-based view for listing posts
class PostListView(ListView):
    model = Post
    template_name = "blog_app/home.html"
    context_object_name = "posts"
    ordering = ["-date_created"]

# Class-based view for displaying a single post
class PostDetailView(DetailView):
    model = Post

# View to create a new post (Requires login)
@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # Set the logged-in user as the author
            new_post.save()
            messages.success(request, "Post created successfully!")
            return redirect('post-detail', pk=new_post.pk)  # ✅ Use pk for consistency
    else:
        form = CreatePostForm()
    
    return render(request, "blog_app/create_post.html", {"form": form})

# View to update an existing post (Requires login)
@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # ✅ Use pk for consistency

    if request.user != post.author:
        messages.error(request, "You are not authorized to update this post.")
        return redirect("post-detail", pk=post.pk)

    if request.method == "POST":
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect("post-detail", pk=post.pk)
    else:
        form = UpdatePostForm(instance=post)

    return render(request, "blog_app/update_post.html", {"form": form, "post": post})

# View to list posts by a specific user (Publicly accessible)
def user_posts(request, user_id):
    user = get_object_or_404(User, pk=user_id)  # ✅ Use pk for consistency
    user_posts = Post.objects.filter(author=user).order_by("-date_created")

    return render(request, "blog_app/user_post.html", {"posts": user_posts, "author": user})  # ✅ Correct data passed

# View to delete a post (Requires login)
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # ✅ Use pk for consistency

    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect("post-detail", pk=post.pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect("blog-home")

    return render(request, "blog_app/delete_post.html", {"post": post})

# About page
def about(request):
    return render(request, "blog_app/about.html", {"title": "About"})

# Contact page
def contact(request):
    return render(request, "blog_app/contact.html")

from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog_app.urls")),
    path("register/", users_views.register, name="users-register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='home'), name="users-logout"),  # Use built-in LogoutView
    path("profile/", users_views.user_profile, name="users-profile"),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

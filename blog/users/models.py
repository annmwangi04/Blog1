from django.db import models
from django.contrib.auth.models import User
from PIL import Image  

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="profile_pics/default.jpeg")
    
    def __str__(self):
        return f"{self.user.username}-profile"
    
    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
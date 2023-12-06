from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Increase max_length to 200
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title
    
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
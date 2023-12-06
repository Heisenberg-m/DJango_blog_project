from django.contrib import admin
from .models import BlogPost,UserProfile

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','author')  # Customize the displayed fields

admin.site.register(BlogPost, BlogPostAdmin)  # Register the model with the admin site
admin.site.register(UserProfile)
from django.db import models

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    # Create relationship django.contrib.auth.models.User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes
    portfolio_site = models.URLField(blank=True)
    
    # pip install pillow to use this!    
    profile_pic = models.ImageField(upload_to='user_auth_app/profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

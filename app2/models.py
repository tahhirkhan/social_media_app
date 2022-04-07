from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=500)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

    


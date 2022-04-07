from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    # comments = models.ManyToManyField(User, related_name='comments')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='name_rel',  on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ' | ' + str(self.comment)


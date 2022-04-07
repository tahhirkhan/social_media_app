from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewPost/str<pk>/', views.viewPost, name='viewPost'),
    path('addPost', views.createPost, name='addPost'),
    path('addCategory', views.addCategory, name='addCategory'),

    path('editPost/str<pk>/', views.editPost, name='editPost'),
    path('deletePost/str<pk>/', views.deletePost, name='deletePost'),
    path('message', views.message, name='message'),

    path('category/str<catgs>/', views.categoryPosts, name='categoryPosts'),
    path('allCategories', views.allCategories, name='allCategories'),
    path('allComments/str<pk>/', views.allComments, name='allComments'),

    path('likePost/str<likeid>/', views.likePost, name='likePost'),
    path('usersPosts', views.usersPosts, name='usersPosts'),
    path('usersLikedPosts', views.usersLikedPosts, name='usersLikedPosts'),
    path('commonProfilePage/str<pk>/', views.commonProfilePafe, name='common'),
    path('addComment/str<pk>/', views.addComment, name='addComment'),
    
]


from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm


# class editUser(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))
   
#     class Meta:
#         model = User
#         fields = ['username', 'email']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

    




class editUserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border-info'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-info'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-info'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(editUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control border-info'


class passwordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'type':'password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control border-primary'}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-primary'}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-primary'}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-primary'}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-primary'}))
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url']

from django.shortcuts import redirect, render
from .models import *
from .forms import CreateUserForm, editUserForm, passwordForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


# def registerUser(request):
    
    
#     if request.method == 'POST':
        
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']


#         user = User.objects.create_user(
#             username=username, email=email, password=password, first_name=firstname, last_name=lastname)
#         user.save()

#         return redirect('login')

    

#     return render(request, 'app2/register.html', )
def registerUser(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'app2/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return redirect('login')

    return render(request, 'app2/login.html')


def addProfilePage(request):
    user = request.user
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']
            website_url = form.cleaned_data['website_url']
            facebook_url = form.cleaned_data['facebook_url']
            instagram_url = form.cleaned_data['instagram_url']
            twitter_url = form.cleaned_data['twitter_url']
            newProfile = Profile(user=user,avatar=avatar, bio=bio, website_url=website_url, facebook_url=facebook_url, instagram_url=instagram_url, twitter_url=twitter_url)
            newProfile.save()
            return redirect('userProfile')
    context_dict = {
        'form': form
    }
    return render(request, 'app2/addProfilePage.html',context_dict)

def editProfilePage(request):
    user = request.user
    user_instance = user.profile
    form = ProfileForm(instance=user_instance)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('userProfile')
        else:
            form = ProfileForm(instance=user_instance) 


    context_dict = {
        'form': form,
    }
    return render(request, 'app2/editProfilePage.html', context_dict)


def logoutUser(request):

    logout(request)
    return redirect('login')

def userProfile(request):
    user = request.user
    firstName = user.first_name
    lastName = user.last_name
    uName = user.username
    email = user.email
    password = user.password
    context_dict = {
        'firstName': firstName,
        'lastName': lastName,
        'username': uName,
        'email': email,
        'password': password,

    }
    return render(request, 'app2/userProfile.html', context_dict)


def editUser(request):
    user = request.user
    form = editUserForm(instance=user)
    if request.method == 'POST':
        form = editUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('eidtMessage')
    context_dict = {
        'form': form,
    }
    return render(request, 'app2/editUser.html', context_dict)


class PasswordsChangeView(PasswordChangeView):
    form_class = passwordForm
    template_name = 'app2/changePassword.html'
    success_url = reverse_lazy('passwordMessage')


def passwordMessage(request):
    return render(request, 'app2/passwordMessage.html')


def editMessage(request):
    return render(request, 'app2/editMessage.html')

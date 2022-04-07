from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('userProfile', views.userProfile, name='userProfile'),
    path('editProfile', views.editUser, name='editUser'),
    path('password', views.PasswordsChangeView.as_view(), name='changePassword'),
    path('passwordMessage', views.passwordMessage, name='passwordMessage'),
    path('editMessage', views.editMessage, name='eidtMessage'),
    path('addProfilePage', views.addProfilePage, name='addProfilePage'),
    path('editProfilePage', views.editProfilePage, name='editProfielPage'),
    
    


]

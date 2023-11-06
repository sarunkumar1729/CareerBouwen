from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('check_username/', views.check_username, name='check_username'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.edit_profile,name='edit_profile')
]
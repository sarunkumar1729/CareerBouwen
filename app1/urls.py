from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('check_username/', views.check_username, name='check_username'),

]
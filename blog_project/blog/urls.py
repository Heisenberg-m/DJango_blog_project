from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('home/',views.home,name='home'),
    path('createpost/',views.createpost,name='createpost'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('profile/',views.profile,name='profile'),
    path('userlogout/',views.userlogout,name='userlogout'),
]


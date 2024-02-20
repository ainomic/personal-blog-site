from django.contrib import admin
from django.urls import path,include
from ainomic_blog import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('signup',views.signUser,name='signup'),
    path('logout',views.logoutUser,name='logout'),
    path('addblog',views.addblog,name='addblog'),
    path('readblog',views.read,name='blogsection')
]
from django.contrib import admin
from django.urls import path,include
from ainomic_blog import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login_user,name='login'),
    path('signup',views.sign_user,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('readblog/<int:id>',views.read_blog,name='readblog'),
]
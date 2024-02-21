from django.contrib import admin
from django.urls import path,include
from ainomic_blog import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login_user,name='login'),
    path('signup',views.sign_user,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('add',views.add_content,name='add'),
    path('blogs/<int:id>',views.view_blog,name='viewblog'),
]
from django.contrib import admin
from django.urls import path,include
from ainomic_blog import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login_user,name='login'),
    path('signup',views.sign_user,name='signup'),
    path('logout',views.logout_user,name='logout'),
    path('blogs/add',views.add_blog,name='add_blog'),
    path('blogs/<int:id>',views.view_blog,name='view_blog'),
    path('update/<int:id>',views.update_content,name='update'),
    path('blogs/delete/<int:id>',views.delete_blog,name='delete_blog'),
]
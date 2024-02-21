from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ainomic_blog.models import Blog

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    blog_list=Blog.objects.order_by('-date_updated')
    return render(request,"dashboard.html",{"blog_list":blog_list})

def login_user(request):
    context={"message":"Not valid"}
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,"login.html",context)
    return render(request,"login.html")

def sign_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = User.objects.create_user(email,"-",password)
        user.save()
        return redirect("/login")
    return render(request,"signup.html")

def logout_user(request):
    logout(request)
    return redirect("/login")

def view_blog(request,id):
    blog_list=Blog.objects.get(id=id)
    return render(request,"view_blog.html",{"blog_list":blog_list})

def add_content(request):
    if request.method=="POST":
        tle=request.POST.get("title")
        descrip=request.POST.get("description")
        wrds=len(descrip.split())
        bl=blogs(title=tle,words=wrds,desc=descrip)
        bl.save()
        return redirect("/")
    return render(request,"add.html")

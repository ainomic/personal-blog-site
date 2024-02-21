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
    try:
        blog_list=Blog.objects.get(id=id)
        return render(request,"view_blog.html",{"blog_list":blog_list})
    except:
        return render(request,"errorpage.html")

def add_blog(request):
    if request.method=="POST":
        blog_title=request.POST.get("title")
        blog_desc=request.POST.get("description")
        wrds=len(blog_desc.split())
        create_blog=Blog(title=blog_title,words=wrds,desc=blog_desc)
        create_blog.save()
        return redirect("/")
    return render(request,"add.html")

def update_content(request,id):
    if request.method=="POST":
        tle=request.POST.get("title")
        descrip=request.POST.get("description")
        bl1=Blog.objects.get(id=id)
        bl1.title=tle
        bl1.desc=descrip
        bl1.save()
        return redirect("/readblog/" + str(id))
    bl=Blog.objects.get(id=id)
    return render(request,"update.html",{"bl":bl})


def delete_blog(request,id):
    blog_list = Blog.objects.get(id=id)
    blog_list.delete()
    return redirect("/")
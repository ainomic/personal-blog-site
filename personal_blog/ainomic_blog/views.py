from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ainomic_blog.models import blog


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    bl = blog.objects.order_by('-id')
    return render(request,"blogpage.html",{"bl":bl})

def loginUser(request):
    context={
        "message":"Not valid"
    }
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,"login.html",context)
    return render(request,"login.html")

def signUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = User.objects.create_user(username,email,password)
        user.save()
        return redirect("/login")
    return render(request,"signup.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def addblog(request):
    if request.method=="POST":
        tle=request.POST.get("title")
        descrip=request.POST.get("description")
        descwords=len(descrip.split())
        bl = blog(title=tle,words=descwords,desc=descrip)
        bl.save()
        return redirect("/")
    return render(request,"addpage.html")

def read(request):
    return render(request,"viewblog.html")
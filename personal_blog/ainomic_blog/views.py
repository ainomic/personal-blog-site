from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ainomic_blog.models import blogs

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    bl=blogs.objects.order_by('-id')
    return render(request,"dashboard.html",{"bl":bl})

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

def read_blog(request,id):
    bl=blogs.objects.get(id=id)
    return render(request,"readblogs.html",{"bl":bl})

def add_content(request):
    if request.method=="POST":
        tle=request.POST.get("title")
        descrip=request.POST.get("description")
        wrds=len(descrip.split())
        bl=blogs(title=tle,words=wrds,desc=descrip)
        bl.save()
        return redirect("/")
    return render(request,"add.html")

def update_content(request,id):
    if request.method=="POST":
        tle=request.POST.get("title")
        descrip=request.POST.get("description")
        bl1=blogs.objects.get(id=id)
        bl1.title=tle
        bl1.desc=descrip
        bl1.save()
        return redirect("/readblog/" + str(id))
    bl=blogs.objects.get(id=id)
    return render(request,"update.html",{"bl":bl})


def delete_blog(request,id):
    bl = blogs.objects.get(id=id)
    bl.delete()
    return redirect("/")
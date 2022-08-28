from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def INDEX(request):
    return render(request,"User/index.html")

def LOGIN(request):
    return render(request,"register/login.html")
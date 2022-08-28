from django.shortcuts import render

def INDEX(request):
    return render(request,"User/index.html")
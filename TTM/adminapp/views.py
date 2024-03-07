from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Admin


# Create your views here.

def ttmhome(request):
    return render(request, "ttmhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = (request.POST("uname"))
        adminpwd = (request.POST("pwd"))
    flag=Admin.objects.filter(username=adminuname,password=adminpwd).values()
    if flag:
        return render(request, "adminhome.html")
    else:
        return HttpResponse("Login fail")

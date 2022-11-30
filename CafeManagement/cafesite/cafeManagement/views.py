from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
import requests




def acIndex(request):
    return render(request,"cafeManagement/base.html")

def acLogout(request):
    return render(request,"/account/login")

def acLogin(request):
   return render(request,"cafeManagement/login.html")

def acForm(request):
    if request.method == "GET":
        form = AccountForm()  
        return render(request,"cafeManagement/form.html",{"form":form})
    else:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("cafeManagement/list.html")

def acView(request):
    return render(request,"cafeManagement/view.html")

def acUpdate(request):
    return render(request,"cafeManagement/update.html")

def acDelete(request):
    return render(request,"cafeManagement/delete.html")

def acList(request):
    response=requests.get("http://127.0.0.1:5000/user").json()
    return render(request,"cafeManagement/list.html",{'response':response})
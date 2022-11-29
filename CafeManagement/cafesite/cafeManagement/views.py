from django.shortcuts import render

# Create your views here.
def acLogin(request):
    return render(request,"cafeManagement/login.html")

def acForm(request):
    return render(request,"cafeManagement/form.html")

def acView(request):
    return render(request,"cafeManagement/view.html")

def acUpdate(request):
    return render(request,"cafeManagement/update.html")

def acDelete(request):
    return render(request,"cafeManagement/delete.html")

def acList(request):
    return render(request,"cafeManagement/list.html")
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import auth


# Create your views here.
from userregsitrationapp.forms import userregisterform


def admin(request):
    return render(request, 'admin.html')

def admincheck(request):
    if request.method == 'POST':
        adminame = request.POST['adminname']
        password = request.POST['password']

        if adminame == 'admin' and password == 'admin':
            return render(request, 'adminhome.html')
        else:
            messages.success(request, 'Invalid user id and password')
        return render(request, 'admin.html')

def adminlogout(request):
    auth.logout(request)
    return redirect('/')

def adminusertab(request):
    return render(request, 'Products_Sold.html')

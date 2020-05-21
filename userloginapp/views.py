from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.models import auth
from .forms import userloginform

def userlogin(request):
    next = request.GET.get('next')
    form = userloginform(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['uname']
        password = form.cleaned_data['paswd']

        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)
        return render(request, 'User.html')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def userlogout(request):
    auth.logout(request)
    return redirect('/')
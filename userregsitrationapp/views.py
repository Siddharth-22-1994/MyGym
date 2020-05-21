from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from userregsitrationapp.forms import userregisterform


def signup(request):
    next = request.GET.get('next')
    form = userregisterform(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('passowrd')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return render(request, 'User.html')


    return render(request, 'signup.html', {'form':form})

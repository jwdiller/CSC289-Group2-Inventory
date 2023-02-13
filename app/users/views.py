from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('!!Sign Up Successful!!'))
            return redirect('home')
        else:
            messages.error(request, ('Error in creating user'))
            return(request, 'users/register.html', {'form' : form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('!!Log In Successful!!'))
            return redirect('home')
        else:
            messages.error(request, ('Password or username incorrect'))
            return(request, 'users/login.html', {'form' : form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html', {'form': form})

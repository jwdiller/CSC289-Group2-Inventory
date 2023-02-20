from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request,('!!Sign Up Successful!!'))
            return redirect('home')
        else:
            messages.error(request, ('Error in creating user'))
            return render(request, 'users/register.html', {'form' : form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':

        user = authenticate(username=username, password=password)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            form.save()
            messages.success(request,('!!Log In Successful!!'))
            return redirect('home')
        else:
            messages.error(request, ('Password or username incorrect'))
            return(request, 'users/login.html', {'form' : form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html', {'form': form})

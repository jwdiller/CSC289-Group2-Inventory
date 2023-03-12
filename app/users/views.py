from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# This initializes the register form that stores the data from the fields into the database
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

# This takes the data from the fields and checks the database for its respective user
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
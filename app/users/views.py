from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordUserChangeForm, cssThemeForm
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
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)

from django.shortcuts import render

def error_403(request, exception):
    return render(request, 'users/403.html', status=403)

def update_theme(request):
    if request.method == 'POST':
        form = cssThemeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = cssThemeForm(instance=request.user)
    return render(request, 'update_theme.html', {'form': form})

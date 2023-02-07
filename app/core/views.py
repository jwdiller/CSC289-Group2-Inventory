from django.shortcuts import render
import random # for the about page, can delete later
from .models import * # All models for the databases
from .forms import * #For forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
	firstpart = random.choice(['Grand', 'Evil', 'Uncouth', 'Mighty'])
	secondpart = random.choice(['Lord', 'Bandit', 'Master'])
	return render(request, 'about.html', {'name': firstpart + " " + secondpart})

def customer(request):
    return render(request, 'customer-db.html', { 'tableitems': Customers.objects.all})

def customersignup(request):
    return render(request, 'core/customer-signup.html', {})

def customersignupSubmit(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Sign Up Successful'))
    return render(request, 'home.html', {})
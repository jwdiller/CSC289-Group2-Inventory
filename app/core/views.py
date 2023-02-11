from django.shortcuts import render
import random # for the about page, can delete later
from .models import * # All models for the databases
from .forms import * #For forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def isAuthorized(request): #need to write this
    return;

def home(request):
    return render(request, 'home.html', {})

def about(request):
	firstpart = random.choice(['Grand', 'Evil', 'Uncouth', 'Mighty'])
	secondpart = random.choice(['Lord', 'Bandit', 'Master'])
	return render(request, 'about.html', {'name': firstpart + " " + secondpart})

def customer(request):
    return render(request, 'customer-db.html', { 'tableitems': Customers.objects.all})

def customersignup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Sign Up Successful'))
            return redirect('home')
    return render(request, 'core/customer-signup.html', {})

def suppliersignup(request):
	if request.method == 'POST':
		form = SupplierForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Supplier Added'))
			return redirect('home')
	else:
		form = SupplierForm()
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Supplier', 'formHeader' : 'Register a Supplier here'})

def stocksignup(request):
	if request.method == 'POST':
		form = StockForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Product Added'))
			return redirect('home')
	else:
		form = StockForm()
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Product Entry', 'formHeader' : 'Register a Project here'})

def ordersignup(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Outgoing Order Added'))
			return redirect('home')
	else:
		form = OrderForm()
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Outgoing Order', 'formHeader' : 'Register an Outgoing Order here'})

def incomingsignup(request):
	if request.method == 'POST':
		form = IncomingForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Incoming Order Added'))
			return redirect('home')
	else:
		form = IncomingForm()
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Incoming Order', 'formHeader' : 'Register an Incoming Order here'})
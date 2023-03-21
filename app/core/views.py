from django.shortcuts import render
import random # for the about page, can delete later
from .models import * # All models for the databases
from .forms import * #For forms
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from better_profanity import profanity
from .fakepop import *
from .query import *
import decimal

# Create your views here.

def isAuthorized(request): #need to write this
	return

# Calls the home.html page for display
def home(request):
    alert_messages(request)
    return render(request, 'home.html', {})

# Generates random words and then calls the about.html page for display (using these words)
# We most likely will change this later :/
def about(request):
    return render(request, 'about.html', {})

# These will call the database.html file and send the responding database that will be shown for the user
def customer(request):
	return render(request, 'database.html', {'title' : 'Customer', 'tableitems' : Customers.objects.all})
def supplier(request):
	return render(request, 'database.html', {'title' : 'Supplier', 'tableitems' : Suppliers.objects.all})
def stock(request):
	return render(request, 'database.html', {'title' : 'Stock', 'tableitems' : Stock.objects.all})
def order(request):
	return render(request, 'database.html', {'title' : 'Order', 'tableitems' : Orders.objects.all})
def incoming(request):
	return render(request, 'database.html', {'title' : 'Incoming', 'tableitems' : Incoming.objects.all})
def dbhome(request):
	return render(request, 'database.html', {})

# Calls the create-entry.html file, this html in question is linked to the core/forms.py file on what form fields be displayed
def signuphome(request):
	return render(request, 'core/create-entry.html', {})

# This function confirms that the form for the 'Add Customer' page has been fully filled out and saves it's contents
def customersignup(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,('Sign Up Successful'))
			return redirect('home')
	else:
		form = CustomerForm()
	# formTitle is the Title for Tab, formHeader is human-readable on the page itself
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Customer', 'formHeader' : 'Register a Customer Here'})

# This function confirms that the form for the 'Add Supplier' page has been fully filled out, validates the data, and then saves its contents
def suppliersignup(request):
	if request.method == 'POST':
		form = SupplierForm(request.POST)
		if form.is_valid():
			name = form.data.get('name')
			if (profanity.contains_profanity(name)):
				messages.error(request,('Inappropriate/Invalid name, please try again!'))
			else:
				form.save()
				messages.success(request,('Supplier Added'))
				return redirect('home')
	else:
		form = SupplierForm()
	# formTitle is the Title for Tab, formHeader is human-readable on the page itself
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Supplier', 'formHeader' : 'Register a Supplier Here'})

# This function confirms that the form for the 'Stock New Product' page has been fully filled out, validates the data, and then saves its contents
def stocksignup(request):
	if request.method == 'POST':
		form = StockForm(request.POST)
		if form.is_valid():
			productName = form.data.get('productName')
			productCost = decimal.Decimal(form.data.get('price'))
			productAmount = int(form.data.get('amount'))
			if (profanity.contains_profanity(productName)):
				messages.error(request,('Inappropriate/Invalid product name, please try again!'))
			else:
				if (productCost < 0 or productCost > 1000000): # Acceptable range is $0.00 - $10,000 dollars
					messages.error(request,('price can\'t be less than 0 or greater than 1,000,000 (10,000 dollars), please try again!'))
				else:
					if (productAmount < 0 or productAmount > 1000):  # Acceptable range is 0 - 1000 'amount'
						messages.error(request,('Amount can\'t be less than 0 or greater than 1,000, please try again!'))
					else:
						form.save()
						messages.success(request,('Product Added'))
						return redirect('home')
	else:
		form = StockForm()
	# formTitle is the Title for Tab, formHeader is human-readable on the page itself
	return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Product Entry', 'formHeader' : 'Register a Product Here'})

# This function confirms that the form for the 'New Outgoing Order' page has been fully filled out, validates the data, and then saves its contents
def ordersignup(request):
    alert_messages(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.userId = request.user
            orderAmount = int(form.data.get('amount'))
            orderCost = decimal.Decimal(form.data.get('price'))
            isValid = True
            if (orderAmount < 0):  # Acceptable range is 1 - 1000 'amount'
                messages.error(request,('Amount can not be less than 0, please try again!'))
                isValid = False
            elif (orderAmount > Stock.objects.values('amount').filter(id=entry.stockID.id)[0]['amount']):
                isValid = False
                messages.error(request,('Amount can not be greater than Current Stock, please try again!'))
            elif (orderAmount > 1000): #Cannot be greater than 1000
                messages.error(request,('Amount can not be greater than 1,000, please try again!'))
                isValid = False
            if (orderCost < 0 or orderCost > 1000000):  # Acceptable range is $0.01 - $10,000 dollars
                messages.error(request,('price can\'t be less than 0 or greater than 1,000,000 (10,000 dollars), please try again!'))
                isValid = False
            if isValid:
                #form.save()
                entry.date = datetime.now()
                entry.save()
                messages.success(request,('Outgoing Order Added'))
                return redirect('home')
    else:
        form = OrderForm()
    # formTitle is the Title for Tab, formHeader is human-readable on the page itself
    return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Outgoing Order', 'formHeader' : 'Register an Outgoing Order Here', 'priceList' : priceList(request)})

# This function confirms that the form for the 'New Incoming Order' page has been fully filled out, validates the data, and then saves its contents
def incomingsignup(request):
    alert_messages(request)
    if request.method == 'POST':
        form = IncomingForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.userId = request.user
            orderAmount = int(form.data.get('amount'))
            orderCost = decimal.Decimal(form.data.get('price'))
            isValid = True
            if (orderAmount < 0 or orderAmount > 1000):  # Acceptable range is 1 - 1000 'amount'
                messages.error(request,('Amount can\'t be less than 0 or greater than 1,000, please try again!'))
                isValid = False
            if (orderCost < 0 or orderCost > 1000000):  # Acceptable range is $0.01 - $10,000 dollars
                messages.error(request,('price can\'t be less than 0 or greater than 1,000,000 (10,000 dollars), please try again!'))
                isValid = False
            if isValid:
                #form.save()
                entry.date = datetime.now()
                entry.save()
                messages.success(request,('Incoming Order Added'))
                return redirect('home')
    else:
        form = IncomingForm()
    # formTitle is the Title for Tab, formHeader is human-readable on the page itself
    return render(request, 'core/create-entry.html', {'form': form, 'formTitle' : 'Create Incoming Order', 'formHeader' : 'Register an Incoming Order Here', 'priceList' : priceList(request)})
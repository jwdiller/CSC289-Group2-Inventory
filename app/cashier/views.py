from django.shortcuts import render
from .query import *

# Create your views here.

# Calls the 
def cashier(request):
    return render(request, 'cart.html', {})

def catalog(request):
    list = getSuppliersAndProducts()
    return render(request, 'catalog.html', {'list':list,})
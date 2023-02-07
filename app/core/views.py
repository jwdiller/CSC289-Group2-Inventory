from django.shortcuts import render
import random # for the about page, can delete later
from .models import * # All models for the databases

# Create your views here.

def about(request):
	firstpart = random.choice(['Grand', 'Evil', 'Uncouth', 'Mighty'])
	secondpart = random.choice(['Lord', 'Bandit', 'Master'])
	return render(request, 'about.html', {'name': firstpart + " " + secondpart})


def customer(request):
    return render(request, 'customer-db.html', { 'tableitems': Customers.objects.all})

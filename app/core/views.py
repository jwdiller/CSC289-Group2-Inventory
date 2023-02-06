from django.shortcuts import render
import random

# Create your views here.

def about(request):
	firstpart = random.choice(['Grand', 'Evil', 'Uncouth', 'Mighty'])
	secondpart = random.choice(['Lord', 'Bandit', 'Master'])
	return render(request, 'about.html', {'name': firstpart + " " + secondpart})

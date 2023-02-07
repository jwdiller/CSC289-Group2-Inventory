from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
	path('', views.home, name='home'),
 	path('database/customer', views.customer, name='customer'), # Start of database URLS
  	path('signup', views.customersignup, name='signup'), # Sign up
	path('signupSUBMIT', views.customersignupSubmit, name='signupSUBMIT')
]

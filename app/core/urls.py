from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.about, name='about'), #about us, experimental page
	path('', views.home, name='home'), #home page
 	path('database/customer', views.customer, name='customer'), # Start of database URLS
  	path('signup', views.customersignup, name='signup'), # Sign up\
    path('create/supplier', views.suppliersignup, name='suppliersignup'),
    path('create/stock', views.stocksignup, name='stocksignup'),
    path('create/order', views.ordersignup, name='ordersignup'),
    path('create/incoming', views.incomingsignup, name='incomingsignup'),
]

from django.urls import path
from .forms import *
from . import views

# These represent the url locations for each page
urlpatterns = [
	path('about/', views.about, name='about'), #about us, experimental page
	path('', views.home, name='home'), #home page
 
 	path('database/customer', views.customer, name='customerDB'), # Start of database URLS
  path('database/supplier', views.supplier, name='supplierDB'), # Add to
  path('database/stock', views.stock, name='stockDB'),          # core/templates/database.html
  path('database/order', views.order, name='orderDB'),
  path('database/incoming', views.incoming, name='incomingDB'),
  path('database/', views.dbhome, name='DB-home'), # Also this line to the general navbar base.html
  path('top_5_stocks/', views.top_5_stocks, name='top_5_stocks'), # Top 5 Stocks (Query)
  
  path('create/customer', views.customersignup, name='customersignup'), # Sign up
  path('create/supplier', views.suppliersignup, name='suppliersignup'), # Add to
  path('create/stock', views.stocksignup, name='stocksignup'),          # core/templates/core/create-entry.html
  path('create/order', views.ordersignup, name='ordersignup'),
  path('create/incoming', views.incomingsignup, name='incomingsignup'),
  path('create/', views.signuphome, name ='signup-home'), # Also add this line to the general navbar base.html
  
  #populate for testing
  path('populate', views.populate, name='populate'),
  
  #Custom Queries
  path('query/month/<int:month>/id/<int:id>', views.query, name='query'),
]

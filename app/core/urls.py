from django.urls import path
from .forms import *
from . import views


urlpatterns = [
	path('about/', views.about, name='about'), #about us, experimental page
	path('', views.home, name='home'), #home page
 
 	path('database/customer', views.customer, name='customerDB'), # Start of database URLS
  path('database/supplier', views.supplier, name='supplierDB'),
  path('database/stock', views.stock, name='stockDB'),
  path('database/order', views.order, name='orderDB'),
  path('database/incoming', views.incoming, name='incomingDB'),
  path('database/', views.dbhome, name='DB-home'),
  
  
  	path('create/customer', views.customersignup, name='customersignup'), # Sign up\
    path('create/supplier', views.suppliersignup, name='suppliersignup'),
    path('create/stock', views.stocksignup, name='stocksignup'),
    path('create/order', views.ordersignup, name='ordersignup'),
    path('create/incoming', views.incomingsignup, name='incomingsignup'),
    path('create/', views.signuphome, name ='signup-home'),
    # sign up, generalized
    #"""path('create/customer', views.signup(ftype = CustomerForm, title = 'Create Customer', header = 'Register a Customer here'), name='customersignup'),
    #path('create/supplier', views.signup(ftype = SupplierForm, title = 'Create Supplier', header = 'Register a Supplier here'), name='suppliersignup'),
    #path('create/stock', views.signup(ftype = StockForm, title = 'Create Product', header = 'Register a Product Here'), name='customersignup'),
    #path('create/order', views.signup(ftype = OrderForm, title = 'Create a New Outgoing Order', header = 'Create a New Outgoing Order'), name='customersignup'),
    #path('create/incoming', views.signup(ftype = IncomingForm, title = 'Create a New Incoming Order', header = 'Create a New Incoming Order'), name='customersignup'),"""
]

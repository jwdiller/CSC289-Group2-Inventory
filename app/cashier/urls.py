from django.contrib import admin
from django.urls import path, include
from users.views import register, login
from django.contrib.auth import views as auth_views
from . import views, cashier

# These represent the url locations for each page
urlpatterns = [
  path('', views.cashier, name='cashier'), # Cashier Page
  path('catalog', views.catalog, name='catalog'), # Catalog View
  path('catalogHandler', cashier.catalogHandler, name='catalogHandler'), # Form action
  
  path('testReceipt', cashier.testReceipt, name='testReceipt'), # For testing purposes
]
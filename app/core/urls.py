from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
 	path('database/customer', views.customer, name='customer'), # Start of database URLS
]

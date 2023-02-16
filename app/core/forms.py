from django import forms
from .models import *
from django.contrib.auth import get_user_model

class CustomerForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Customers
		fields = ["userName", "email", "phoneNumber", "note"]
  
class SupplierForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Suppliers
		fields = ["name", "email", "phoneNumber", "note"]

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["productName", "upc",	"cents", "number", "description", "supplierID"]

class OrderForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Orders
		fields = ["userId", "customerId", "stockID", "amount", "date", "shortnote", "note", "cents"]

class IncomingForm(forms.ModelForm):
	class Meta:
		model = Incoming
		fields = ["userId", "supplierId", "stockID", "amount", "date", "shortnote", "note", "cents"]
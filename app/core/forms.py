from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customers
		fields = ["userName", "email", "phoneNumber", "note"]
  
class SupplierForm(forms.ModelForm):
	class Meta:
		model = Suppliers
		fields = ["name", "email", "phoneNumber", "note"]

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["productName", "upc",	"cents", "number", "description", "supplierID"]

class OrderForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ["userId", "customerId", "stockID", "amount", "date", "shortnote", "note", "cents"]

class IncomingForm(forms.ModelForm):
	class Meta:
		model = Incoming
		fields = ["userId", "supplierId", "stockID", "amount", "date", "shortnote", "note", "cents"]
from django import forms
from .models import *
from django.contrib.auth import get_user_model
# This creates the customer form fields for the "Add Customer" page
class CustomerForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Customers
		fields = ["userName", "email", "phoneNumber", "note"]

# This creates the supplier form fields for the "Add Supplier" page
class SupplierForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Suppliers
		fields = ["name", "email", "phoneNumber", "note"]

# This creates the stock form fields for the "Stock New Product" page
class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["productName", "upc",	"cents", "amount", "description", "supplierID"]

# This creates the outgoing order form fields for the "New Outgoing Order" page
class OrderForm(forms.ModelForm):
	date = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Orders
		fields = ["userId", "customerId", "stockID", "amount", "date", "shortnote", "note", "cents"]

# This creates the incoming order form fields for the "New Incoming Order" page
class IncomingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Incoming
        fields = ["userId", "supplierId", "stockID", "amount", "date", "shortnote", "note", "cents"]

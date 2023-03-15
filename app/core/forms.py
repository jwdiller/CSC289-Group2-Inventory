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
		fields = ["productName", "upc",	"price", "amount", "description", "supplierID"]

# This creates the outgoing order form fields for the "New Outgoing Order" page
class OrderForm(forms.ModelForm):
	#date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.now())
	stockID = forms.ModelChoiceField(queryset=Stock.objects.all(), label = "Stock ID")
	stockID.widget.attrs.update({'onchange' : 'onChangeStock()'})
	amount = forms.IntegerField(help_text="Limit to Maximum Current Stock")
	amount.widget.attrs.update({'oninput' : "onChangeAmount()"})
	price = forms.DecimalField(help_text="Per Unit Price")
	price.widget.attrs.update({'oninput' : 'onChangePrice()'})
	class Meta:
		model = Orders
		fields = ["customerId", "stockID", "amount",  "price", "shortnote", "note",]
		labels = {'stockID' : 'Stock ID'}

# This creates the incoming order form fields for the "New Incoming Order" page
class IncomingForm(forms.ModelForm):
    #date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.now())
    class Meta:
        model = Incoming
        fields = ["supplierId", "stockID", "amount", "price", "shortnote", "note",]

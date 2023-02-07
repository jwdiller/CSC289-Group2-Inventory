from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customers
		fields = ["userName", "email", "phoneNumber", "note"]
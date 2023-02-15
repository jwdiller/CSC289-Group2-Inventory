from django.db import models
from django.conf import settings

class Customers(models.Model):
    userName = models.CharField(max_length=200, verbose_name='User Name')
    email = models.EmailField(max_length=200, verbose_name='E-Mail')
    phoneNumber = models.CharField(max_length=50, verbose_name="Phone Number")
    note = models.CharField(max_length=200, verbose_name='Note')

    def __str__(self):
        return self.userName

class Suppliers(models.Model):
    name = models.CharField(max_length=200, verbose_name="Supplier Name")
    email = models.EmailField(max_length=200, verbose_name="E-Mail")
    phoneNumber = models.CharField(max_length=50, verbose_name="Phone Number")
    note = models.CharField(max_length=200, verbose_name="Note")

    def __str__(self):
        return self.name


class Stock(models.Model):
    productName = models.CharField(max_length=200, verbose_name="Product Name")
    upc = models.IntegerField(verbose_name="UPC") #ID for 'outside world'
    cents = models.IntegerField() #In cents - needs function wrapping. Not using float because of precision
    number = models.IntegerField(verbose_name="Amount") #As a generic inventory item, integer
    description = models.CharField(max_length=200, verbose_name="Description")
    supplierID = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name="Supplier ID")

    def __str__(self):
        return str(self.upc) + " " + str(self.productName)
    def price(self):
        return self.cents/100

class Orders(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Authorizer ID")
    customerId = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, verbose_name="Customer ID")
    stockID = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, verbose_name="Stock ID")
    amount = models.IntegerField(verbose_name="Amount") # As this is now generalized, using integer instead
    date = models.DateTimeField(verbose_name="Date and Time")
    shortnote = models.CharField(max_length=20, verbose_name="Short Note")
    note = models.CharField(max_length=200, verbose_name="Note") # May be needed
    cents = models.IntegerField() # While amount * stockPrice would be default, this changes

    def __str__(self):
        return str(self.date) + " " + str(self.stockID) + " " + str(self.shortnote)
    def price(self):
        return self.cents / 100

class Incoming(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Authorizer ID")
    supplierId = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True, verbose_name="Supplier ID")
    stockID = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, verbose_name="Stock ID")
    amount = models.IntegerField(verbose_name="Amount") # As this is now generalized, using integer instead
    date = models.DateTimeField()
    shortnote = models.CharField(max_length=20, verbose_name="Short Note")
    note = models.CharField(max_length=200, verbose_name="Note") # May be needed
    cents = models.IntegerField() # While amount * stockPrice would be default, this changes

    def __str__(self):
        return str(self.date) + " " + str(self.stockID) + " " + str(self.shortnote)
    def price(self):
        return self.cents / 100







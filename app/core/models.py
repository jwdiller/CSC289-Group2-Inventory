from django.db import models
from django.conf import settings
from datetime import datetime


#All functions in here representthe values that will be stored in their respective databases
# This creates the values that will be held in the Customers database
class Customers(models.Model):
    userName = models.CharField(max_length=200, verbose_name='User Name')
    email = models.EmailField(max_length=200, verbose_name='E-Mail')
    phoneNumber = models.CharField(max_length=50, verbose_name="Phone Number")
    note = models.CharField(max_length=200, verbose_name='Note', blank=True,)

    # __str__ statement in order to present a readable format
    def __str__(self):
        return self.userName

# This creates the values that will be held in the Suppliers database
class Suppliers(models.Model):
    name = models.CharField(max_length=200, verbose_name="Supplier Name")
    email = models.EmailField(max_length=200, verbose_name="E-Mail")
    phoneNumber = models.CharField(max_length=50, verbose_name="Phone Number")
    note = models.CharField(max_length=200, verbose_name="Note", blank=True,)

    # __str__ statement in order to present a readable format
    def __str__(self):
        return self.name

# This creates the values that will be held in the Stock database
class Stock(models.Model):
    productName = models.CharField(max_length=200, verbose_name="Product Name")
    upc = models.IntegerField(verbose_name="UPC") #ID for 'outside world'
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Price Per Unit") # Nevermind, it seems that DecimalField is the answer all along
    amount = models.IntegerField(default=0, verbose_name="Amount") # Generic Item-Integer, Current Stock, so should be modified by new Orders and Incoming
    description = models.CharField(max_length=200, verbose_name="Description", blank=True,)
    supplierID = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name="Supplier ID")

    # __str__ statement in order to present a readable format
    def __str__(self):
        return str(self.upc) + " " + str(self.productName)

# This creates the values that will be held in the Orders database (Outgoing Orders)
class Orders(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Authorizer ID")
    customerId = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, verbose_name="Customer ID")
    stockID = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, verbose_name="Stock ID")
    amount = models.IntegerField(verbose_name="Amount") # Generalized, uses Integer. Subtracts from stock.amount
    date = models.DateTimeField(verbose_name="Date and Time")
    shortnote = models.CharField(max_length=20, verbose_name="Short Note", blank=True,)
    note = models.CharField(max_length=200, verbose_name="Note", blank=True,) # May be needed
    price = models.DecimalField(decimal_places=2, max_digits=6) # While amount * stockPrice would be default, this changes

    # __str__ and price statement in order to present a readable format
    def __str__(self):
        return str(self.date) + " " + str(self.stockID) + " " + str(self.shortnote)
    
    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)

        # Update the stock amount
        stock = Stock.objects.get(id=self.stockID.id)
        stock.amount -= self.amount
        stock.save()

# This creates the values that will be held in the Incoming database (Incoming Orders)
class Incoming(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Authorizer ID")
    supplierId = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True, verbose_name="Supplier ID")
    stockID = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, verbose_name="Stock ID")
    amount = models.IntegerField(verbose_name="Amount") # Generalized, uses Integer. Adds from stock.amount
    date = models.DateTimeField(verbose_name="Date and Time")
    shortnote = models.CharField(max_length=20, verbose_name="Short Note", blank=True,)
    note = models.CharField(max_length=200, verbose_name="Note", blank=True,) # May be needed
    price = models.DecimalField(decimal_places=2, max_digits=6) # While amount * stockPrice would be default, this changes

    # __str__ and price statement in order to present a readable format
    def __str__(self):
        return str(self.date) + " " + str(self.stockID) + " " + str(self.shortnote)

    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)

        # Update the stock amount
        stock = Stock.objects.get(id=self.stockID.id)
        stock.amount += self.amount
        stock.save()

# Database of who we are going to pay taxes to

class salesTax(models.Model):
    tax = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateTimeField(verbose_name="Date and Time")
    
    def __str__(self):
        return str(self.date) + " $" + str(self.tax)

"""
class TaxEntity(models.Model):
    taxPercent = models.DecimalField(decimal_places = 4, max_digits=10) # Assume every item has the same % for now
    address = models.CharField(max_length=200, verbose_name="Address")
    email = models.EmailField(max_length=200, verbose_name='E-Mail')
    phoneNumber = models.CharField(max_length=50, verbose_name="Phone Number")
    note = models.CharField(max_length=200, verbose_name='Note', blank=True,)
        
# CART creates outgoing carts, which are groups of outgoing Orders with with the same customer and time stamps.
class Cart(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Authorizer ID")
    customerId = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, verbose_name="Customer ID")
    date = models.DateTimeField(verbose_name="Date and Time")
    
    shortnote = models.CharField(max_length=20, verbose_name="Short Note", blank=True,)
    note = models.CharField(max_length=200, verbose_name="Note", blank=True,) # May be needed
    
    subTotal = models.JSONField() #StockID, amount, price
    tax = models.DecimalField(decimal_places=2, max_digits=6) # Should be a % from TaxEntity
    taxEntityID = models.ForeignKey(TaxEntity, on_delete=models.SET_NULL, null=True, verbose_name="Paying Taxes To: ") # If a mobile business, can cross county lines
    """
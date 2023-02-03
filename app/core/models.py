from django.db import models
class Orders(models.Model):
    userId = models.IntegerField()
    customerId = models.IntegerField()
    stockID = models.IntegerField()
    amount = models.IntegerField() # As this is now generalized, using integer instead
    date = models.DateTimeField()
    shortnote = models.CharField(max_length=20)
    note = models.CharField(max_length=200) # May be needed
    cents = models.IntegerField() # While amount * stockPrice would be default, this changes

    def __str__(self):
        return str(self.date) + " " + str(self.stockID) + " " + str(self.shortnote)
    def price(self):
        return self.cents / 100

class Stock(models.Model):
    productName = models.CharField(max_length=200)
    upc = models.IntegerField() #ID for 'outside world'
    cents = models.IntegerField() #In cents - needs function wrapping. Not using float because of precision
    number = models.IntegerField() #As a generic inventory item, integer
    description = models.CharField(max_length=200)
    supplierID = models.IntegerField()

    def __str__(self):
        return str(self.upc) + " " + str(self.productName)
    def price(self):
        return self.cents/100


class Customers(models.Model):
    userName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.userNameclass

Suppliers(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=50)
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.name

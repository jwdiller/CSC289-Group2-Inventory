from .models import *
from .forms import *
import random
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

#name, email, phoneNumber, note
entitySQL = '''
INSERT INTO
% s (%s, %s, %s, %s)
VALUES
(%s, %s, %s, %s, %s);
'''
        
def fakeCustomerModel():
    firstName = ['Abby', 'Bob', 'Charlie', 'Debbie', 'Egon']
    lastName = ['Smith', 'Brown', 'Carpenter', 'Erikson']
    eProvide = ['google.com', 'my.waketech.edu', 'yahoo.com']
    fLen = len(firstName)
    lLen = len(lastName)
    eLen = len(eProvide)
    total_num = fLen * lLen
    for i in range(total_num):
        fName = firstName[i % fLen]
        lName = lastName[i % lLen]
        name = fName + ' ' + lName
        email = fName[:1].lower() + lName.lower() + '@' + eProvide[i % eLen]
        pNumber = random.randint(0, 9999999999)
        new = Customers()
        new.userName = name
        new.email = email
        new.phoneNumber = pNumber
        new.note = ''
        new.save()
        
def fakeSupplierModel():
    names = ['Acme, Inc.', "Raynor's Refreshments, LLC", "Ice Cream Pirates Group"]
    email = ['sales@acme.org', 'support@raynorrefresh.com', 'contact@icpg.org']
    notes = ['Suppliers of Fine Dynamite', 'Off Fighting Zerg', 'Found the One Piece']
    total_num = len(names)
    for i in range(total_num):
        pNumber = random.randint(0, 9999999999)
        new = Suppliers()
        new.name = names[i]
        new.email = email[i]
        new.phoneNumber = pNumber
        new.note = notes[i]
        new.save()
        
def fakeStockModel():
    brands = ["Acme", "Raynor's", "Piratastic"]
    flavors = ["Vanilla", "Chocolate", "Strawberry"]
    sizes = ['Pint', 'Half Gallon']
    sIDs = Suppliers.objects.raw('SELECT id FROM core_suppliers')
    num_brands = len(brands)
    for i in range(num_brands):
        for flavor in flavors:
            for size in sizes:
                brand = brands[i]
                new = Stock()
                new.productName = brand + " " + flavor + " " + size + " Ice Cream"
                new.upc = random.randint(0, 1000000)
                new.cents = random.randint(199, 799)
                new.amount = random.randint(10, 100)
                new.description = ''
                new.supplierID = sIDs[i]
                new.save()
                
#["userId", "customerId", "stockID", "amount", "date", "shortnote", "note", "cents"]

def fakeInOutModel():
    numdays = 2000 # a bit over 5 years
    today = datetime.now()
    userIDs = User.objects.raw('SELECT id FROM auth_user')
    customerIDs = Customers.objects.raw('SELECT id FROM core_customers')
    supplierIDs = Suppliers.objects.raw('SELECT id FROM core_suppliers')
    stockIDs = Stock.objects.raw('SELECT id FROM core_stock')
    u_stock = len(stockIDs)
    stockAmounts = [100] * u_stock
    for day in range(numdays, 0, -1):
        newOrder = Orders()
        newOrder.userId = random.choice(userIDs) # change to random
        day = today - timedelta(days = day)
        newOrder.date = day
        newOrder.customerId = random.choice(customerIDs)
        stockIndex = random.randint(0, u_stock-1)
        newOrder.stockID = stockIDs[stockIndex]
        amount = random.randint(1, 5)
        newOrder.amount = amount
        stockAmounts[stockIndex] = stockAmounts[stockIndex] - amount
        newOrder.shortnote = ''
        newOrder.note = ''
        newOrder.cents = random.randint(199, 799) * amount
        newOrder.save()
        if stockAmounts[stockIndex] < 30:
            newIn = Incoming()
            newIn.userId = random.choice(userIDs)
            newIn.supplierId = random.choice(supplierIDs) # NEEDS TO BE BETTER
            newIn.stockID = stockIDs[stockIndex]
            newIn.amount = 50
            newIn.date = day
            newIn.shortnote = ''
            newIn.note = ''
            newIn.cents = random.randint(25, 199) * amount
            newIn.save()
            
def populate(request):
    Customers.objects.all().delete()
    Suppliers.objects.all().delete()
    Stock.objects.all().delete()
    Orders.objects.all().delete()
    Incoming.objects.all().delete()
    random.seed(0)
    fakeCustomerModel()
    fakeSupplierModel()
    fakeStockModel()
    fakeInOutModel()
    messages.success(request,('Populated Database'))
    return render(request, 'home.html', {})
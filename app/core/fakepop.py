from .models import *
from .forms import *
import random
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from decimal import Decimal

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
    brands = {"Acme" : 1, "Raynor's" : 1.2, "Piratastic" : 1.5,}
    flavors = {"Vanilla" : 1, "Chocolate" : 1.4, "Strawberry" : 1.25}
    sizes = {'Pint' : 1, 'Half Gallon' : 2}
    sIDs = Suppliers.objects.raw('SELECT id FROM core_suppliers')
    #num_brands = len(brands)
    for brand, supplier in zip(brands, sIDs):
        for flavor in flavors:
            for size in sizes:
                #brand = brands[i]
                new = Stock()
                new.productName = brand + " " + flavor + " " + size + " Ice Cream"
                new.upc = random.randint(0, 1000000)
                new.price = (random.randrange(150, 200)/100) + (brands[brand] * flavors[flavor] * sizes[size])
                new.amount = 100
                new.description = ''
                new.supplierID = supplier
                new.save()
                
#["userId", "customerId", "stockID", "amount", "date", "shortnote", "note", "price"]

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
        newOrder.price = amount * (1.25) * Stock.objects.values('price').filter(id=newOrder.stockID)[0]
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
            newIn.price = amount * (.75) * Stock.objects.values('price').filter(id=newOrder.stockID)[0]
            newIn.save()
                        
def fakeInOut2(days):
    numdays = days # 2000 for five years
    today = datetime.now()
    
    userIDs = User.objects.order_by('id')
    customerIDs = Customers.objects.raw('SELECT id FROM core_customers')
    stocks = Stock.objects.raw('SELECT id, price, supplierID_id FROM core_stock')
    supplierIDs = Suppliers.objects.raw('SELECT id FROM core_suppliers')
    
    stockAmounts = {}
    restoreAmount = 70
    for stock in stocks:
        stockAmounts[stock] = 100
    
    for day in range(numdays, 0, -1):
        currentday = today - timedelta(days=day)
        if day % 7 == 0:
            for stock, amount in zip(stocks, stockAmounts):
                if stockAmounts[amount] <= 30:
                    newIncom = Incoming()
                    newIncom.date = currentday
                    newIncom.userId = userIDs[0]
                    newIncom.amount = restoreAmount
                    newIncom.shortnote = ''
                    newIncom.note = ''
                    stockAmounts[amount] = stockAmounts[amount] + restoreAmount
                    newIncom.stockID = stock
                    #newIncom.supplierId = stock['supplierID_id']
                    newIncom.supplierId = random.choice(supplierIDs)
                    newIncom.price = restoreAmount * product.price * random.randrange(25,50) / 100
                    newIncom.save()
        else:
            onRegister = random.choice(userIDs)
            for customer in customerIDs:
                if random.randint(1, 4) == 1:
                    newOrder = Orders()
                    newOrder.userId = onRegister
                    newOrder.shortnote = ''
                    newOrder.note = ''
                    newOrder.customerId = customer
                    amount = random.randint(1, 5)
                    newOrder.amount = amount
                    product = random.choice(stocks)
                    newOrder.stockID = product
                    price = amount * product.price * random.randrange(125,150) / 100
                    newOrder.price = price
                    rightNow = currentday + timedelta(hours=random.randint(0,23), minutes=random.randint(0,59), seconds=random.randint(0,59))
                    newOrder.date = rightNow
                    stockAmounts[product] = stockAmounts[product] - amount
                    newOrder.save()
                    newTax = salesTax()
                    newTax.tax = price * Decimal(.07) # CHANGE THIS IN THE FUTURE
                    newTax.date = rightNow
                    newTax.save()
                    

def populate(request, days):
    fakeInOut2(days)
    messages.success(request,('Populated Database from ' + str(days) + ' days to today.'))
    return render(request, 'home.html', {})
            
def repop(request, days=2000):
    Customers.objects.all().delete()
    Suppliers.objects.all().delete()
    Stock.objects.all().delete()
    Orders.objects.all().delete()
    Incoming.objects.all().delete()
    salesTax.objects.all().delete()
    random.seed(0)
    fakeCustomerModel()
    fakeSupplierModel()
    fakeStockModel()
    fakeInOut2(days)
    messages.success(request,('Repopulated Database'))
    return render(request, 'home.html', {})

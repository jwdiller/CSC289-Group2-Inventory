from core.models import Orders, Stock, Customers, salesTax
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from .query import *
from decimal import Decimal

def catalogHandler(request):
    list = getSuppliersAndProducts()
    isValid = True
    """print({k:v[0] for k,v in dict(request.POST).items()})
    amountDictionary = {k: v for k, v in request.POST if k.startswith("amount-")}
    print("amountDictionary : ", amountDictionary)
    discountDictionary = {k: v for k, v in request.POST if k.startswith("discount-")}
    print("discountDictionary : ", discountDictionary)"""
    amountDictionary = {}
    discountDictionary = {}
    requestDictionary = dict(request.POST).items()
    for entry in requestDictionary:
        print(entry, "\n")
        if entry[0].startswith("amount-"):
            try:
                amountDictionary[entry[0]] = int(entry[1][0])
            except:
                amountDictionary[entry[0]] = 0
        elif entry[0].startswith("discount-"):
            try:
                discountDictionary[entry[0]] = Decimal(entry[1][0])
            except:
                discountDictionary[entry[0]] = 0
       
    for product in amountDictionary:
        if amountDictionary[product] < 0:
            isValid = False
    for product in discountDictionary:
        if discountDictionary[product] < 0:
            isValid = False
    if isValid:
        rightNow = datetime.now()
        cashierID = request.user
        try:
            customerID = Customers.objects.filter(phoneNumber=request.POST['customerPhone'])[0]
        except:
            customerID = None
        print("customer is ", customerID)
        subTotal = 0
        for product in amountDictionary:
            if amountDictionary[product] and amountDictionary[product] > 0:
                newOrder = Orders()
                newOrder.userId = cashierID
                newOrder.date = rightNow
                newOrder.stockID = Stock.objects.filter(id=int(product[7:]))[0]
                newOrder.amount = amountDictionary[product]
                ourPrice = Stock.objects.values("price").filter(id=int(product[7:]))[0]['price']
                miniTotal = (newOrder.amount * ourPrice) - discountDictionary["discount" + product[6:]]
                subTotal += miniTotal
                newOrder.price = miniTotal
                newOrder.customerId = customerID
                newOrder.shortnote = ''
                newOrder.note = ''
                #print(newOrder)
                newOrder.save()
        newTax = salesTax()
        newTax.date = rightNow
        newTax.tax = subTotal * Decimal(.0725) # Should change this in the future
        #print(newTax)
        newTax.save()
        messages.success(request, "Cart Successful")
        return render(request, 'cashierScreen.html', {})
    messages.error(request, "Error in Processing Cart, starting over.")
    return render(request, 'catalog.html', {'list':list,})
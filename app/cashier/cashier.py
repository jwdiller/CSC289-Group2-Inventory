from core.models import Orders, Stock, Customers, salesTax
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from .query import *
from decimal import Decimal
#import json
import simplejson as json
from django.core.mail import send_mail

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
        receiptDict = {'rightNow' : rightNow.strftime("%A %B %d, %Y %X %Z"), 'products' : [],}
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
                receiptDict['products'].append({'name' : Stock.objects.values("productName").filter(id=int(product[7:]))[0]['productName'][:25],'amount' : str(amountDictionary[product]), 'price' : str(ourPrice), 'discount' : str(discountDictionary["discount" + product[6:]]), 'total' : str(miniTotal)})
                newOrder.save()
        newTax = salesTax()
        newTax.date = rightNow
        newTax.tax = subTotal * Decimal(.0725) # Should change this in the future
        receiptDict['subTotal'] = "%.2f" % subTotal
        receiptDict['tax'] = "%.2f" % newTax.tax
        receiptDict['total'] = "%.2f" % (subTotal + newTax.tax)
        #receiptDict['email'] = Customers.objects.values('email').filter(id=customerID)[0]['email']
        if customerID is not None:
            receiptDict['email'] = Customers.objects.filter(id=customerID.id).first().email
        #print(newTax)
        newTax.save()
        print(receiptDict)
        messages.success(request, "Cart Successful")
        return render(request, 'cashierScreen.html', {'receiptDict' : json.dumps(receiptDict), 'email' : receiptDict['email']})
    messages.error(request, "Error in Processing Cart, starting over.")
    return render(request, 'catalog.html', {'list':list,})

def testReceipt(request):
    testDict = {'rightNow' : datetime.now().strftime("%A %B %d, %Y %X %Z"), 'products' : []}
    
    testDict['products'].append({'name' : 'Questionable Life Choices', 'amount' : "5", 'price' : "1.55", 'discount' : "2", 'total' : "5.75"})
    testDict['products'].append({'name' : 'Chuuni Daydreams', 'amount' : "10", 'price' : "0.50", 'discount' : "0", 'total' : "5.00"})
    testDict['subTotal'] = "10.75"
    testDict['tax'] = ".78"
    testDict['total'] = "11.53"
    testDict['email'] = 'jwdiller@my.waketech.edu'
    
    return render(request, 'cashierScreen.html', {'receiptDict' : json.dumps(testDict), 'email' : 'jwdiller@my.waketech.edu'})

def emailReceipt(request):
    receiptDict = json.loads(request.POST['receiptDict'])
    print(request.POST['emailAddress'])
    
    outputString = receiptDict['rightNow']
    outputString += "\n\n"
    
    for product in receiptDict['products']:
        outputString += "\n" + product['name'] + "\t" + product['price'] + " x "  + product['amount']
        outputString += "\n\t\t -" + product['discount'] + " = " + product['total'] + "\n"
        
    outputString += "\n\nSubTotal : " + receiptDict['subTotal']
    outputString += "\nTax : " + receiptDict['tax']
    outputString += "\nTotal : " + receiptDict['total']
    
    outputString += "\n\nThank you for shopping with us!"
    
    try:
        send_mail(subject="Receipt from Small Store", message=outputString, from_email=None, recipient_list=[request.POST['emailAddress']], fail_silently=False,)
        messages.success(request, "Receipt Emailed to " + request.POST['emailAddress'])
    except:
        messages.error(request, "Could not send email.")
    
    return render(request, 'cashierScreen.html', {})
from django.shortcuts import render
from .models import *
from django.db import connection
from datetime import *
from dateutil.relativedelta import relativedelta 
from django.db.models import Sum
from django.contrib import messages

def getProducts():
    return Stock.objects.values('id', 'productName')

def getOrders(month, id):
    return Orders.objects.filter(date__gte=datetime.now() - relativedelta(months = month)).filter(stockID=id)

def formatDate(raw_date):
    return raw_date.strftime('%Y-%m-%d:%H:%M:%SZ')

def getLastWeekOrders():
    return Orders.objects.filter(date__gte=datetime.now() - relativedelta(weeks = 1)).annotate(order_amount=Sum('amount'))

def numbersold(request, month, id):
    raw_data = getOrders(month, id)
    title = 'Amount Sold for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    products = getProducts()
    
    amount_over_time = [{'t' : formatDate(datetime.now() - relativedelta(months = month)), 'y' : 0}]
    currentAmount = 0
    for order in raw_data:
        currentAmount = currentAmount + order.amount
        amount_over_time.append({ 't' : formatDate(order.date), 'y' : currentAmount})
    amount_over_time.append({'t' : formatDate(datetime.now()), 'y' : currentAmount})
    
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'amt' : currentAmount, 'chartlabel' : 'Amount Sold'})


## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## !!! MUST ADD IN INCOMING ORDERS IN ORDER TO FINISH !!!
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def profit(request, month, id):
    raw_data = getOrders(month, id)
    title = 'Profit for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    products = getProducts()
    
    amount_over_time = [{'t' : formatDate(datetime.now() - relativedelta(months = month)), 'y' : 0}]
    currentProfit = 0
    for order in raw_data:
        currentProfit = currentProfit + float("{:.2f}".format(order.cents/100))
        amount_over_time.append({ 't' : formatDate(order.date), 'y' : currentProfit})
    amount_over_time.append({'t' : formatDate(datetime.now()), 'y' : currentProfit})
    currentProfit = "{:.2f}".format(currentProfit)
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'profit' : currentProfit, 'chartlabel' : 'Profits'})

# For inventory alerts, more work needed.

def inventoryAlerts():
    alertLists = [[],[]]
    orders = getLastWeekOrders()
    products = getProducts()
    for product in products:
        if product.amount < orders[product].Sum:
            alertLists[0].append(product.id)
        elif product.amount < orders[product].Sum * 2:
            alertLists[1].append(product.id)
        #elif product.amount < product.max * .3
            #alertLists[2].append(product.id)
    return alertLists

def alert_messages():
    alert = inventoryAlerts()
    for product in alert[0]:
        messages.warning('WARNING! ' + product.productName + ' stock predicted to run out within the week!',extra_tags='High Priority')
    for product in alert[1]:
        messages.warning('Warning : ' + product.productName + ' stock predicted to run out within two weeks.',extra_tags='Medium Priority')
    #for product in alert[2]:
        #messages.warning(product.productName ' stock running low.', extra_tags:'Low Priority')
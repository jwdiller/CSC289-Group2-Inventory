from django.shortcuts import render
from .models import *
from django.db import connection
from datetime import *
from dateutil.relativedelta import relativedelta  

def getProducts():
    return Stock.objects.values('id', 'productName')

def getOrders(month, id):
    return Orders.objects.filter(date__gte=datetime.now() - relativedelta(months = month)).filter(stockID=id)

def numbersold(request, month, id):
    raw_data = getOrders(month, id)
    title = 'Amound Sold for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    products = getProducts()
    
    amount_over_time = []
    currentAmount = 0
    for order in raw_data:
        currentAmount = currentAmount + order.amount
        amount_over_time.append({ 't' : order.date.strftime('%Y-%m-%d:%H:%M:%SZ'), 'y' : currentAmount})
    
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'amt' : currentAmount, 'chartlabel' : 'Amount Sold'})


## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## !!! MUST ADD IN INCOMING ORDERS IN ORDER TO FINISH !!!
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def profit(request, month, id):
    raw_data = getOrders(month, id)
    title = 'Profit for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    products = getProducts()
    
    amount_over_time = []
    currentProfit = 0
    for order in raw_data:
        currentProfit = currentProfit + float("{:.2f}".format(order.cents/100))
        amount_over_time.append({ 't' : order.date.strftime('%Y-%m-%d:%H:%M:%SZ'), 'y' : currentProfit})
    currentProfit = "{:.2f}".format(currentProfit)
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'profit' : currentProfit, 'chartlabel' : 'Profits'})
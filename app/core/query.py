from django.shortcuts import render
from .models import *

def getProducts():
    return Stock.objects.values('id', 'productName')

def numbersold(request, month, id):
    products = getProducts()
    currentAmount = 0
    title = 'Moo'
    return render(request, 'chart.html', {'title' : title, 'data' : [], 'currentMonth' : month, 'currentID' : id, 'products' : products, 'amt' : currentAmount, 'chartlabel' : 'Amount Sold'})

def profit(request, month, id):
    currentProfit = 0
    title = 'Moo'
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'profit' : currentProfit, 'chartlabel' : 'Profits'})

def numbersold2(request, month, id):
    query = '''
    SELECT *
    FROM core_orders
    WHERE
    date >= date('now', '-%s month')
    AND
    stockID_id = %s
    ORDER BY
    date
    '''
    raw_data = Orders.objects.raw(query %(month, id))
    title = 'Order Query for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    query2 = '''
    SELECT id, productName
    FROM core_stock
    '''
    products = Stock.objects.raw(query2)
    
    amount_over_time = []
    currentAmount = 0
    for order in raw_data:
        currentAmount = currentAmount + order.amount
        amount_over_time.append({ 't' : order.date.strftime('%Y-%m-%d:%H:%M:%SZ'), 'y' : currentAmount})
    
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'amt' : currentAmount, 'chartlabel' : 'Amount Sold'})


## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## !!! MUST ADD IN INCOMING ORDERS IN ORDER TO FINISH !!!
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def profit2(request, month, id):
    query = '''
    SELECT *
    FROM core_orders
    WHERE
    date >= date('now', '-%s month')
    AND
    stockID_id = %s
    ORDER BY
    date
    '''
    raw_data = Orders.objects.raw(query %(month, id))
    title = 'Order Query for the last ' + str(month) + ' month(s) of Stock ID #' + str(id)
    query2 = '''
    SELECT id, productName
    FROM core_stock
    '''
    products = Stock.objects.raw(query2)
    
    amount_over_time = []
    currentProfit = 0
    for order in raw_data:
        currentProfit = currentProfit + float("{:.2f}".format(order.cents/100))
        amount_over_time.append({ 't' : order.date.strftime('%Y-%m-%d:%H:%M:%SZ'), 'y' : currentProfit})
    currentProfit = "{:.2f}".format(currentProfit)
    return render(request, 'chart.html', {'title' : title, 'data' : amount_over_time, 'currentMonth' : month, 'currentID' : id, 'products' : products, 'profit' : currentProfit, 'chartlabel' : 'Profits'})
from .models import Stock,Orders
from django.db.models import Sum
from django.db import connection



# This function is used to get the top amount of items in a model.
def find_top_amount():
    query = """
    SELECT core_stock.productName, SUM(core_orders.amount) AS orderAmount
    FROM core_orders
    INNER JOIN core_stock ON core_orders.stockId_id = core_stock.id
    GROUP BY core_orders.stockID_id
    ORDER BY orderAmount DESC
"""

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    top_5_stocks = (
    Orders.objects
    .select_related('stockID') # To prefetch the related Stock object
    .values('stockID__productName') # Group by product name
    .annotate(order_amount=Sum('amount')) # Calculate the sum of amount for each stock
    .order_by('-order_amount') # Sort by descending order_amount
    .values('stockID__productName', 'order_amount')[:5] # Select top 5 results
    )
    return results


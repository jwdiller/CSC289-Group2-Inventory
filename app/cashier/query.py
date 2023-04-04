from core.models import *

def getSuppliersAndProducts():
    nested_list = {}
    suppliers = Suppliers.objects.values('id', 'name')
    for supplier in suppliers:
        getID = supplier['id']
        nested_list[getID] = {'supplierName' : supplier['name'], 'products' : list(Stock.objects.values("productName", "id", "price", "amount").filter(supplierID=getID))}
    return nested_list
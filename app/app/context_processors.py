# Self defined context processors

def getSingleProductId(request):
    from core.models import Stock
    try:
        return {'singleProductID' : Stock.objects.values('id')[0]['id']}
    except:
        return {'singleProductID' : -1}
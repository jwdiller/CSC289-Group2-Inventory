from django.contrib import admin
from .models import *

admin.site.register(Customers)
admin.site.register(Suppliers)
admin.site.register(Stock)
admin.site.register(Orders)

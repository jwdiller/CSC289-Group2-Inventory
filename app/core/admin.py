from django.contrib import admin
from .models import *

# This registers the following databases for the admin page so admins can see them
admin.site.register(Customers)
admin.site.register(Suppliers)
admin.site.register(Stock)
admin.site.register(Orders)
admin.site.register(Incoming)
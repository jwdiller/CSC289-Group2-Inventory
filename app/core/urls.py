from django.urls import path
from .forms import *
from . import views, query
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import *
# These represent the url locations for each page
urlpatterns = [
  path('', views.home, name='home'), #home page
	path('about/', views.about, name='about'), #about us, experimental page
  
  # Start of database URLS
 	path('database/customer', views.customer, name='customerDB'), # Start of database URLS
  path('database/supplier', views.supplier, name='supplierDB'), # Add to
  path('database/stock', views.stock, name='stockDB'),          # core/templates/database.html
  path('database/order', views.order, name='orderDB'),
  path('database/incoming', views.incoming, name='incomingDB'),
  path('database/', views.dbhome, name='DB-home'), # Also this line to the general navbar base.html
  
  # Start of create URLS
  path('create/customer', views.customersignup, name='customersignup'), # Sign up
  path('create/supplier', views.suppliersignup, name='suppliersignup'), # Add to
  path('create/stock', views.stocksignup, name='stocksignup'),          # core/templates/core/create-entry.html
  path('create/order', views.ordersignup, name='ordersignup'),
  path('create/incoming', views.incomingsignup, name='incomingsignup'),
  path('create/', views.signuphome, name ='signup-home'), # Also add this line to the general navbar base.html
  
  #populate for testing
  path('reseed', views.repop, name='repop'),
  path('reseed/<int:days>', views.repop, name='minirepop'),
  path('populate/<int:days>', views.populate, name='populate'),
  
  #Custom Queries
  path('chart/sold/month/<int:month>/id/<int:id>', query.numbersold, name='numsold'),
  path('chart/profit/month/<int:month>/id/<int:id>', query.profit, name='profit'),

  #profile
  path('profile/', profile , name='profile'),
  #password reset
  path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
  path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
  path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
  path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'), 
#path('top_5_stocks/', views.top_5_stocks, name='top_5_stocks'), # Top 5 Stocks (Query)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

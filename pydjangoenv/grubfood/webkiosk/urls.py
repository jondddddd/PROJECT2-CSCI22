#crating the url urlpatterns
from django.urls import path
#have to link urls.py to views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#need a "." to look at the same folder u exist
#include funtion allows us to include other stuff
app_name = 'webkiosk'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerpage, name='register-page'),
    path('login/', views.loginpage, name='login-page'),
    path('logout/', views.logoutUser, name='logout-page'),

    path('food/', views.listfood, name='listfood'),
    path('food/new/', views.createfood, name='food-create'),
    path('food/<int:pk>/', views.detailfood, name='food-detail'),
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

    path('Orders/', views.listorders, name='listorders'),
    path('Orders/new/', views.createorders, name='order-create'),
    path('Orders/<int:pk>/', views.detailorders, name='order-details'),
    path('Orders/<int:pk>/edit/', views.updateorders, name='order-update'),
    path('Orders/<int:pk>/delete/', views.deleteorders, name='order-delete'),

    path('Customers/', views.listcustomer, name='listcustomer'),
    path('Customers/new/', views.createcustomer, name='customer-create'),
    path('Customers/<int:pk>/', views.detailcustomer, name='customer-details'),
    path('Customers/<int:pk>/edit/', views.updatecustomer, name='customer-update'),
    path('Customers/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),


    #name is alias or variable name

]

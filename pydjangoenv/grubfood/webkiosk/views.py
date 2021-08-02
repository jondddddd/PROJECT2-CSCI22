from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Food, Orders
from .forms import Foodform, Ordersform, Customerform
from django.contrib import messages

# Create your views here.
#define our view Function
def index(request):
    return render(request, 'webkiosk/welcome.html')
def listfood(request):
    context={
        'foodlist': Food.objects.all(),

    }
    return render(request, 'webkiosk/food.html', context)
def listorders(request):
    context={
        'orderlist': Orders.objects.all(),

    }
    return render(request, 'webkiosk/orders.html', context)
def createorders(request):
    if request.method =='GET':
        form = Ordersform()
    elif request.method =='POST':
        #INSERT NEW FOOD RECORD
        form = Ordersform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order record successfully added')
            return redirect('webkiosk:listfood')
    context = {'form':form}
    return render(request,'webkiosk/food_form.html', context)
def detailorders(request, pk):
    order = Orders.objects.get(id=pk)
    context ={'order': order }
    return render(request, 'webkiosk/order_detail.html', context)
def updateorders(request,pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'GET':
        form = Ordersform(instance=order)
    elif request.method =='POST':
        form = Ordersform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order  successfully updated')
    context = {'form':form}
    return render(request,'webkiosk/orders_form.html',context)
def deleteorders(request,pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'GET':
        context = {'order':order}
        return render(request,'webkiosk/order_delete.html', context)
    elif request.method =='POST':
        order.delete()
        return redirect('webkiosk:listorders')

def listcustomer(request):
    context={
        'customerlist': Customer.objects.all(),

    }
    return render(request, 'webkiosk/customer.html', context)
def createcustomer(request):
    if request.method =='GET':
        form = Customerform()
    elif request.method =='POST':

        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record successfully added')
            return redirect('webkiosk:listcustomer')
    context = {'form':form}
    return render(request,'webkiosk/customer_form.html', context)
def detailcustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={'customer':customer}
    return render(request, 'webkiosk/customer_detail.html', context)
def updatecustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = Customerform(instance=customer)
    elif request.method =='POST':
        form = Customerform(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer details successfully updated')
    context = {'form':form}
    return render(request,'webkiosk/Customer_form.html',context)
def deletecustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = {'customer':customer}
        return render(request,'webkiosk/customer_delete.html', context)
    elif request.method =='POST':
        food.delete()
        return redirect('webkiosk:listcustomer')
        
def createfood(request):
    if request.method =='GET':
        form = Foodform()
    elif request.method =='POST':
        #INSERT NEW FOOD RECORD
        form = Foodform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully added')
            return redirect('webkiosk:listfood')
    context = {'form':form}
    return render(request,'webkiosk/food_form.html', context)
def detailfood(request, pk):
    food = Food.objects.get(id=pk)
    context ={'food':food}
    return render(request, 'webkiosk/food_detail.html', context)
def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = Foodform(instance=food)
    elif request.method =='POST':
        form = Foodform(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated')
    context = {'form':form}
    return render(request,'webkiosk/food_form.html',context)
def deletefood(request,pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food':food}
        return render(request,'webkiosk/food_delete.html', context)
    elif request.method =='POST':
        food.delete()
        return redirect('webkiosk:listfood')

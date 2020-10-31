from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers': customers, 'orders': orders, 'order_count': total_orders, 'orders_delivered':delivered, 'orders_pending':pending}
    return render(request, 'accounts/dashboard.html',  context)

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accounts/products.html', {'products': products})

def customers(request, primk):
    customer = Customer.objects.get(id=primk)

    orders = customer.order_set.all()
    orders_count = orders.count()
    
    context = {'customer': customer, 'orders': orders, 'order_count':orders_count}
    return render(request, 'accounts/customers.html', context)
    
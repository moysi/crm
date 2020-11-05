from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

def createOrder(request):

    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
    
def updateOrder(request, ordpk):

    order = Order.objects.get(id=ordpk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, ordpk):
    order = Order.objects.get(id=ordpk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
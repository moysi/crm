from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accounts/products.html', {'products': products})

def customers(request):
    return render(request, 'accounts/customers.html')
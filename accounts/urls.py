from django.urls import path
from . import views

appname = "accounts"

# Create your views here.
urlpatterns = [
    path('', views.home),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
]

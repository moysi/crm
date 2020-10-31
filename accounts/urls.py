from django.urls import path
from . import views

appname = "accounts"

# Create your views here.
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customers/<str:primk>/', views.customers, name='customers'),
]

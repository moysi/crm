from django.urls import path
from . import views

appname = "accounts"

# Create your views here.
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('products/', views.products, name='products'),
    path('customers/<str:primk>/', views.customers, name='customers'),
    path('account/', views.accountSetings, name='account'),
    path('user/', views.userPage, name='user'),
    path('create_order/<str:primk>', views.createOrder, name='create_order'),
    path('update_order/<str:ordpk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:ordpk>', views.deleteOrder, name='delete_order')
]   

from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('delete_order/<str:ordpk>', views.deleteOrder, name='delete_order'),

    #Django reset password functionality used to reset passwords
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]   



# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
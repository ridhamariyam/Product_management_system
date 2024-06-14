
from django.urls import path
from authentication.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', login_view, name='login'),
    path('signup_customer/', customer_signup_view, name='customer_signup'),
    path('signup_shopkeeper/', shopkeeper_signup_view, name='shopkeeper_signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

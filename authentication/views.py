from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from .models import APIKey
from products.models import User

def customer_signup_view(request):
    if request.method == 'POST':
        print('lllll5555555llll')
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            print('lllllllll')
            user = form.save(commit=False)
            user.role = 'customer'
            user.save()
            api_key = APIKey.objects.create(user=user)
            return redirect('login')
    else:
        form = CustomerSignupForm()
    return render(request, 'registration/signup.html', {'form': form, 'user_type': 'Customer'})

def shopkeeper_signup_view(request):
    if request.method == 'POST':
        form = ShopkeeperSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'storekeeper'
            user.save()
            api_key = APIKey.objects.create(user=user)
            return redirect('login')
    else:
        form = ShopkeeperSignupForm()
    return render(request, 'registration/shopkeeper_signup.html', {'form': form, 'user_type': 'Shopkeeper'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser: 
                login(request, user)
                return redirect('product_list')
            else:
                try:
                    api_key = APIKey.objects.get(user=user)
                    if api_key.is_valid():
                        login(request, user)
                        return redirect('product_list')
                    else:
                        form.add_error(None, 'The API key associated with this account is invalid.')
                except APIKey.DoesNotExist:
                    form.add_error(None, 'No API key found for this user.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

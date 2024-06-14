from products.views import product_list_view
from django.urls import path
from .views import *

urlpatterns = [
    
    
    path('products/', product_list_view, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),    
    path('<int:pk>/update/', product_update, name='product_update'), 
    path('<int:pk>/delete/', product_delete, name='product_delete'),
    path('api/', product_data, name='product_data'),
]

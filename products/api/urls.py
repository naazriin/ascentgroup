from django.urls import path

from products.api.views import product

urlpatterns = [
    path('product', product, name='products'),
    
]
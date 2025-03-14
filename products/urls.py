from django.urls import path
from .views import products, detail

urlpatterns = [
    path('', products, name='products'),
    path('<int:product_id>/',detail, name='detail'),

    
]

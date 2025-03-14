from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='home_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page'),
    
]

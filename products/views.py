from django.shortcuts import render, get_object_or_404

from .models import Product

def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'products': product
    }
    return render(request, 'detail.html', context)



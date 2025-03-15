from django.http import HttpResponse
from products.models import Product

from products.api.serializers import ProductSerializer

def product(request):
    product_list =  Product.objects.all()

    serializer = ProductSerializer(product_list, many=True)
    return HttpResponse(serializer.data)
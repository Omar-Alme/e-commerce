from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    """ A view to return the products page """

    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, "products/products.html", context)
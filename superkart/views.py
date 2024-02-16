from django.shortcuts import render
from product.models import Product
import random


def home(request):
    """View for the home page showing popular products."""
    products = Product.objects.filter(is_available=True).order_by('-price')[:6]

    random_products = random.sample(list(products), min(len(products), 6))


    context = {
        'products': random_products,
    }

    return render(request, "home.html", context)


def handler404(request, exception):
    """Custom 404 error handler"""
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """Custom 500 error handler"""
    return render(request, "errors/500.html", status=500)

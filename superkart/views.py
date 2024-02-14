from django.shortcuts import render
from product.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')	

    context = {
        'products': products,
    }

    return render(request, "home.html", context)


def handler404(request, exception):
    """Custom 404 error handler"""
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """Custom 500 error handler"""
    return render(request, "errors/500.html", status=500)

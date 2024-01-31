from django.shortcuts import render

# Create your views here.
def cart(request):
    """ A view to return the cart page """
    return render(request, "products/cart.html")
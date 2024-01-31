from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Cart, CartItem

# Create your views here.
def cart(request):
    """ A view to return the cart page """
    return render(request, "products/cart.html")



def cart_id(request):
    """ Return the current cart id, create one if doesn't exist """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = cart_id(request)
        )
        cart.save()

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
            cart_item.save()

        return redirect('cart')



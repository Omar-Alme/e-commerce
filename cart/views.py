from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product, Product_options
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    """ A view to return the cart page """

    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2 * total) / 100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, "products/cart.html", context)



def remove_cart_item(request, product_id):
    """ Remove a single item from the cart """

    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_all_cart_item(request, product_id):
    """ Remove all items from the cart """

    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect('cart')


def cart_id(request):
    """ Return the current cart id, create one if doesn't exist """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(id=product_id)
    options = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                product_options = Product_options.objects.get(product=product, option_category__iexact=key, option_value__iexact=value)
                options.append(product_options)
                
            except Product_options.DoesNotExist:
                pass

           
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('cart')



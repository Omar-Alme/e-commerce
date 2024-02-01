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



def remove_cart_item(request, product_id, cart_item_id):
    """ Remove a single item from the cart """

    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


def remove_all_cart_item(request, product_id, cart_item_id):
    """ Remove all items from the cart """

    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
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

    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_option = item.options.all()
            ex_var_list.append(list(existing_option))
            id.append(item.id)

        if options in ex_var_list:
            i = ex_var_list.index(options)
            cart_item = CartItem.objects.get(product=product, id=id[i])
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart,
            )

            if len(options) > 0:
                cart_item.options.clear()
                cart_item.options.add(*options)
            cart_item.save()
    else:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        if len(options) > 0:
            cart_item.options.clear()
            cart_item.options.add(*options)
        cart_item.save()

    return redirect('cart')



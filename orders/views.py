from django.shortcuts import render, redirect, reverse
from cart.models import CartItem, Cart
from cart.views import cart_id
from .forms import OrderForm
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
import decimal
import datetime
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_securely(request, total=0, quantity=0, cart_items=None):
    """ A view to return the checkout securely page """
    
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    
    tax = 0
    grand_total = 0
    cart = Cart.objects.get(cart_id=cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

        tax = (2 * total) / 100
        grand_total = total + tax
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address1 = form.cleaned_data['address1']
            data.address2 = form.cleaned_data['address2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.zipcode = form.cleaned_data['zipcode']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            year = int(data.created_at.strftime('%Y'))
            month = int(data.created_at.strftime('%m'))
            day = int(data.created_at.strftime('%d'))
            date = datetime.date(year, month, day)
            current_date = date.strftime('%Y%m%d')
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=user, is_ordered=False, order_number=order_number)

            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'grand_total': grand_total,
                'tax': tax,

            }

            return render(request, 'orders/payments.html', context)
        
    else:
        form = OrderForm()

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'grand_total': grand_total,
        'tax': tax,
        'form': form,
    }

    return redirect('checkout')



@csrf_exempt
def payments(request,):
    """ A view to return the stripe payments page """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':

        
        user = request.user
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)


        line_items = []
        for cart_item in cart_items:
            
            price_with_tax = cart_item.product.price * (1 + decimal.Decimal('0.02'))  # Include tax (2% in this example)
            unit_amount = int(price_with_tax * 100)

            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount':unit_amount ,
                    'product_data': {
                        'images': [request.build_absolute_uri(cart_item.product.image)],
                        'name': cart_item.product.product_name,
                    },
                },
                'quantity': cart_item.quantity,
            })            

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
        return redirect(checkout_session.url, code=303)
        
    return render(request, 'orders/payments.html')


def success(request):
    """ A view to return the success page """

    return render(request, 'orders/success.html')

def cancel(request):

    return render(request, 'orders/cancel.html')
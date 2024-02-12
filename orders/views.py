from django.shortcuts import render, redirect
from cart.models import CartItem, Cart
from cart.views import cart_id
from .forms import OrderForm
from .models import Order
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
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

            return redirect('checkout')
        
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

    # return render(request, 'checkout.html', context)
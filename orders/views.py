from django.shortcuts import render, redirect
from cart.models import CartItem
from .forms import OrderForm
from .models import Order
import datetime

# Create your views here.
def checkout_securely(request, total=0, quantity=0, cart_items=None):
    """ A view to return the checkout securely page """
    user = request.user
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax
    

    cart_items = CartItem.objects.filter(user=user)
    cart_items_count = cart_items.count()
    if cart_items_count <= 0:
        return redirect('products')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
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

        return redirect('checkout')





    return render(request, 'orders/checkout_securely.html')
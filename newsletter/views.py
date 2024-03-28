from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Subscriber

# Create your views here.
def subscribe(request):
    """ A view to subscripe to newsletter """
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'You have successfully subscribed')

            subject = 'You have Subscribed to us! Welcome to DRIPDROP'
            message = 'Thank you for subscribing to our newsletter. We will keep you updated with our latest products and offers.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
    return redirect('/')
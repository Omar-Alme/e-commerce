from django.shortcuts import render, redirect
from django.contrib import messages
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
    return redirect('/')
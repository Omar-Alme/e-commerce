from django.urls import path
from . import views


urlpatterns = [
    path(
        'checkout_securely/', 
        views.checkout_securely, 
        name='checkout_securely'
        ),
    path('payments/', views.payments, name='payments'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')
]
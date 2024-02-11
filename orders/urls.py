from django.urls import path
from . import views


urlpatterns = [
    path('checkout_securely/', views.checkout_securely, name='checkout_securely'),
    
]
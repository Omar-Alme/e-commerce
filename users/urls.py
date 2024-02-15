from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order_history/', views.order_history, name='order_history'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

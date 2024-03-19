from django.contrib import admin
from .models import Order, OrderItem, Payment

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('payment', 'user', 'product', 
                        'quantity', 'price', 'ordered', 'created_at')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 
                    'city', 'order_total', 'tax', 'status', 'is_ordered', 
                    'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 
                    'email']
    list_per_page = 20
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
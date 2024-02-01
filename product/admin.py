from django.contrib import admin
from .models import Product, Product_options

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)

class Product_optionsAdmin(admin.ModelAdmin):
    list_display = ('product', 'option_category', 'option_value', 'is_active', 'created_date')
    list_filter = ('product', 'option_category', 'option_value', 'is_active')
    search_fields = ('product', 'option_category', 'option_value')
    list_editable = ('is_active',)
    
admin.site.register(Product_options, Product_optionsAdmin)

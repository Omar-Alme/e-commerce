from django.contrib import admin
from .models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined')
    search_fields = ('email', 'date_joined')
    list_filter = ('date_joined',)
    ordering = ('-date_joined',)

    
admin.site.register(Subscriber)


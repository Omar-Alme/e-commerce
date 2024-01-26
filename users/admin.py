from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_filter = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from users.models import UserProfile
from django.utils.html import format_html

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


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')



admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
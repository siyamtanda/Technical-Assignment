
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'home_address', 'phone_number', 'location')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('home_address', 'phone_number', 'location')}),
    )

admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)

class CustomAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

custom_admin_site = CustomAdminSite(name='myadmin')
custom_admin_site.register(CustomUser, CustomUserAdmin)


# Register your models here.

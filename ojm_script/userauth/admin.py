from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User,ElectricianProfile,CustomerProfile
class ElectricianProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'country', 'state', 'city')

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'state', 'city')
    
class CustomUserAdmin(UserAdmin):
    # Define the list filters
    list_filter = ('is_active', 'groups')

    search_fields = ('username',)

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

   


admin.site.register(ElectricianProfile, ElectricianProfileAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(User, CustomUserAdmin)

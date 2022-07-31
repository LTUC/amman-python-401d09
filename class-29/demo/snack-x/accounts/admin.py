from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_filter = ('email',)
    search_fields = ["username"]
    list_display = ['email', 'username','first_name']
    fieldsets = (
        ('Auth Info', {
            'fields': ('username','email', 'password')
        }),
        ('Personal Info', {
            'fields' : ('first_name', 'last_name', 'phone_number')
        }),
        ('Dates', {
            'classes': ('collapse',),
            'fields': ('date_joined', 'last_login')
        }),

        ('Permissions', {
            'fields': (

                'is_active',
                'is_staff',
                'is_superuser',
                'user_permissions',
                'groups',
            )
        })
    )
admin.site.register(CustomUser, CustomUserAdmin)
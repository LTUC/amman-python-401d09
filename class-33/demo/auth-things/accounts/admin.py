from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'email', 'password'),
    #     }),
    #     ("Personal Info", {
    #         'fields': ('first_name', 'last_name', 'phone_number')
    #     })
    # )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ("Personal Info", {
            'fields': ('first_name', 'last_name', 'phone_number')
        })
    )
admin.site.register(CustomUser, CustomUserAdmin)

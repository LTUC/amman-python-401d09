from django.contrib import admin

from .models import Snack
# Register your models here.
class CustomSnackAdmin(admin.ModelAdmin):
    model = Snack
    fieldsets = (
        ('Owner', {
            'fields' : ('purchaser',)
        }),
        ('Snack Info', {
            'fields':(
                'name',
                'desc'
            )
        })
    )

    list_display = ('name', 'purchaser')
    list_filter = ('name', 'desc')
    search_fields = ('name', 'desc')
admin.site.register(Snack, CustomSnackAdmin)
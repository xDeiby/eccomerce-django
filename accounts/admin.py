from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):
    # Campos a mostrar
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'date_joined',
        'is_active',
    )

    # Campos que linkean a los detalles
    list_display_link = (
        'email',
        'first_name',
        'last_name',
    )

    # Campos no editables
    readonly_fields = (
        'last_login',
        'date_joined',
    )

    # En orden ascendente segun fecha de registro
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import CustomUser  

@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email',  'date_joined')
    list_filter = ('is_staff',  'date_joined')
    search_fields = ('username', 'email')

    readonly_fields = ('last_login', 'date_joined')

admin.site.unregister(Group)

# Develop: vmgabriel

"""Module for Control of Data admin"""

from django.contrib import admin
from gestionUsuarios.models import User


class UserAdmin(admin.ModelAdmin):
    """Definition for User Admin for Show Only Data User"""
    list_display = ('name', 'email')
    search_fields = ('name', 'tfno', 'email')


# Models
admin.site.register(User, UserAdmin)

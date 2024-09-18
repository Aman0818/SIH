from django.contrib import admin
from .models import Tree

class TreeAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'botanical_name')

admin.site.register(Tree, TreeAdmin)

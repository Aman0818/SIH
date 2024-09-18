from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'tree', 'content', 'created_at', 'updated_at')  
    search_fields = ('user__username', 'tree__common_name') 

admin.site.register(Note, NoteAdmin)
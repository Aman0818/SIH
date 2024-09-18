from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('users/', include('users.urls')),  
    path('trees/', include('trees.urls')),
    path('notes/', include('notes.urls')),

]

admin.site.index_title="👋 Welcome to Admin dashboard"
admin.site.site_header="HackMonks -AYUSH"
admin.site.site_title="HackMonks -AYUSH"
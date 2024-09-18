from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:common_name>/', views.create_note, name='create_note'),
    path('update/<str:common_name>/', views.update_note, name='update_note'), 
    path('delete/<str:common_name>/', views.delete_note, name='delete_note'),  
    path('myNotes/<str:common_name>/', views.get_user_note, name='get_user_note'),
]

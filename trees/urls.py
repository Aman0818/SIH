from django.urls import path
from .views import tree_detail,tree_list

urlpatterns = [
    path('', tree_list, name='tree-list'),
    path('<str:common_name>/', tree_detail, name='tree-detail'),
]
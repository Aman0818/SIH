from django.urls import path
from .views import user_create, user_details,show_all_bookmarks,create_bookmark, remove_bookmark
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('create/', user_create, name='user-create'), 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('details/', user_details, name='user-details'),  
    path('bookmarks/showAllBookmarks/', show_all_bookmarks, name='show_all_bookmarks'),
    path('bookmarks/createBookmark/<str:common_name>/',create_bookmark, name='create_bookmark'),
    path('bookmarks/removeBookmark/<str:common_name>/',remove_bookmark, name='remove_bookmark'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

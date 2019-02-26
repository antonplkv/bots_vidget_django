from django.contrib import admin
from django.urls import path


from .views import * 
urlpatterns = [
    path('', getting_user_info),
    path('view', display_users),
    path('new_users', update_user_page)
    
]

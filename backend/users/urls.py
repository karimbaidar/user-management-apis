from django.urls import path
from . import api

urlpatterns = [
    path('users/', api.user_list),
    path('users/create/', api.create_user),
    path('users/<int:pk>/', api.user_detail), 
]
# menu/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),  # List all menu items
    path('<int:pk>/', views.menu_detail, name='menu_detail'),  # Menu item details
]

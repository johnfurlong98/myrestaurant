# myrestaurant/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists in 'templates/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('accounts/', include('accounts.urls')),  # Accounts app URLs
    path('reservations/', include('reservations.urls')),  # Reservations app URLs
    path('menu/', include('menu.urls')),  # Menu app URLs
]

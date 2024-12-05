# reservations/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_table, name='book_table'),  # Book a table
    path('my-bookings/', views.my_bookings, name='my_bookings'),  # View user's bookings
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),  # Booking details
]

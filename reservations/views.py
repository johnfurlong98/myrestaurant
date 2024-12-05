# reservations/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .models import Booking

@login_required
@role_required('ADMIN')
def admin_booking_management(request):
    """
    Admin view to manage all bookings.
    """
    bookings = Booking.objects.all()
    return render(request, 'reservations/admin_booking_management.html', {'bookings': bookings})

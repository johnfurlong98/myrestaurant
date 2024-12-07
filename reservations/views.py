from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required  # Ensure this decorator exists
from .models import Booking, Table  # Ensure these models are defined
from .forms import BookingForm  # Ensure BookingForm is defined

@login_required
def book_table(request):
    """
    Allow users to book a table.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Optionally, add logic to check table availability
            booking.save()
            return redirect('my_bookings')  # Redirect to the user's bookings page
    else:
        form = BookingForm()
    return render(request, 'reservations/book_table.html', {'form': form})

@login_required
def my_bookings(request):
    """
    Display all bookings made by the current user.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservations/my_bookings.html', {'bookings': bookings})

@login_required
def booking_detail(request, pk):
    """
    Display details of a specific booking.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'reservations/booking_detail.html', {'booking': booking})

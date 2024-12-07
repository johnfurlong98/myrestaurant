# reservations/forms.py

from django import forms
from .models import Booking, Table
from django.utils import timezone

class BookingForm(forms.ModelForm):
    """
    Form for creating a new booking.
    """
    class Meta:
        model = Booking
        fields = ['table', 'guest_count', 'booking_date', 'booking_time', 'special_requests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < timezone.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        # Optional: Add additional time validations if necessary
        return booking_time

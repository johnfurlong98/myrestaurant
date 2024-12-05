from django.db import models

# reservations/models.py

from django.db import models
from django.conf import settings

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    guest_count = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'booking_date', 'booking_time')
        ordering = ['-booking_date', 'booking_time']

    def __str__(self):
        return f"Booking by {self.user.username} on {self.booking_date} at {self.booking_time}"


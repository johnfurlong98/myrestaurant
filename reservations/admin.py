from django.contrib import admin
from .models import Table, Review, Booking
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'is_available')
    search_fields = ('number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'guest_count', 'booking_date', 'booking_time', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'table__number')
    actions = ['mark_as_confirmed', 'mark_as_cancelled']

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='CONFIRMED')
        self.message_user(request, "Selected bookings have been marked as Confirmed.")
    mark_as_confirmed.short_description = "Mark selected bookings as Confirmed"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='CANCELLED')
        self.message_user(request, "Selected bookings have been marked as Cancelled.")
    mark_as_cancelled.short_description = "Mark selected bookings as Cancelled"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'comment')


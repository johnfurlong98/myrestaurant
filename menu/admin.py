# menu/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'dietary_preference', 'image_preview')
    list_filter = ('category', 'is_available', 'dietary_preference')
    search_fields = ('name', 'description')
    ordering = ('category', 'name')
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category', 'dietary_preference', 'is_available')
        }),
        ('Image', {
            'fields': ('image', 'image_preview'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

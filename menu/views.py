# menu/views.py

from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def menu_list(request):
    """
    Display a list of all available menu items.
    """
    items = MenuItem.objects.filter(is_available=True)
    return render(request, '/workspace/myrestaurant/menu/templates/menu_list.html', {'items': items})

def menu_detail(request, pk):
    """
    Display details of a specific menu item.
    """
    item = get_object_or_404(MenuItem, pk=pk, is_available=True)
    return render(request, '/workspace/myrestaurant/menu/templates/menu_detail.html', {'item': item})


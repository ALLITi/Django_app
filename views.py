from django.shortcuts import render
from .models import MenuItem

def draw_menu(request, menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
    except MenuItem.DoesNotExist:
        return ''
    menu_items = menu.get_descendants(include_self=True)
    return render(request, 'menu.html', {'menu_items': menu_items})

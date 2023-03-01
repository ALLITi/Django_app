from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MenuItem
from .forms import MenuItemForm

class MenuItemAdmin(MPTTModelAdmin):
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)

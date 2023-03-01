from django import template
from django.urls import reverse, NoReverseMatch
from ..models import MenuItem
from mptt.templatetags.mptt_tags import cache_tree_children

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
    except MenuItem.DoesNotExist:
        return ''

    request = context['request']
    menu_items = cache_tree_children(menu)

    def make_menu_items(menu_items):
        menu_list = []
        for item in menu_items:
            menu_item = {
                'name': item.name,
                'url': item.url,
                'active': False,
                'children': make_menu_items(item.get_children()),
            }
            if item.url:
                try:
                    url = reverse(item.url)
                    if request.path == url:
                        menu_item['active'] = True
                except NoReverseMatch:
                    pass
            menu_list.append(menu_item)
        return menu_list

    menu_data = make_menu_items(menu_items)
    return context['template'].render({'menu_data': menu_data})

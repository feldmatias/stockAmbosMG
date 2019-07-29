from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def manufacture_color_count(manufacture, color_id):
    if not manufacture:
        return 0

    try:
        item = manufacture.manufactureitem_set.get(color__id=color_id)
        return item.count
    except ObjectDoesNotExist:
        return 0

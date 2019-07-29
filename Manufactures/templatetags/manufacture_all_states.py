from django import template

from Manufactures.models import Manufacture

register = template.Library()


@register.simple_tag
def manufacture_all_states():
    return Manufacture.STATUS

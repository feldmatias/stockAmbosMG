from django import template

from Sales.models import Sale

register = template.Library()


@register.simple_tag
def get_sale_types():
    return Sale.TYPES

from django import template

from Products.models import Product

register = template.Library()


@register.simple_tag
def get_all_products():
    return Product.objects.all().order_by('id')

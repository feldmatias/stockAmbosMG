from django import template

register = template.Library()


@register.simple_tag
def config_items():
    return [
        {
            'name': 'Productos',
            'url': 'stock:index',
            'active': 'productos/'
        }
    ]

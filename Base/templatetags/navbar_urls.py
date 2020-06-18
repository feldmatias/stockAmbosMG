from django import template

register = template.Library()


@register.simple_tag
def navbar_urls():
    return [
        {
            'name': 'Stock',
            'url': 'stock:index',
            'active': 'stock/'
        },
        {
            'name': 'Cortes',
            'url': 'manufactures:index',
            'active': 'cortes/'
        },
        {
            'name': 'Ventas',
            'url': 'sales:index',
            'active': 'ventas'
        },
        {
            'name': 'Configuración',
            'url': 'config:index',
            'active': 'configuracion'
        }
    ]

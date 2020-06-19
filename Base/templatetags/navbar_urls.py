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
            'name': 'Detalle',
            'url': 'sales:index',
            'active': 'detalle'
        },
        {
            'name': 'Configuración',
            'url': 'config:index',
            'active': 'configuracion'
        }
    ]

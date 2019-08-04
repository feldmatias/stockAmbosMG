from extra_views import InlineFormSetFactory

from Products.models import ProductColor


class ProductColorInlineFormset(InlineFormSetFactory):
    model = ProductColor
    fields = ['color']
    prefix = 'color'

    factory_kwargs = {'extra': 0, 'min_num': 1, 'can_delete': True, 'validate_min': True}

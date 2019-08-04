from extra_views import InlineFormSetFactory

from Products.models import ProductSize


class ProductSizeInlineFormset(InlineFormSetFactory):
    model = ProductSize
    fields = ['size']
    prefix = 'talle'

    factory_kwargs = {'extra': 0, 'min_num': 1, 'can_delete': True, 'validate_min': True}

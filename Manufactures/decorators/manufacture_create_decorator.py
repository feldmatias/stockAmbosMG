from Manufactures.models import Manufacture
from Products.decorators.product_bar_decorator import ProductBarDecorator


class ManufactureCreateDecorator(ProductBarDecorator):
    def __init__(self, product):
        super().__init__(product)

    def all_states(self):
        return Manufacture.STATUS

from Manufactures.models import Manufacture
from Products.decorators.product_bar_decorator import ProductBarDecorator


class ManufactureDecorator(ProductBarDecorator):
    def __init__(self, product=None, manufacture=None):
        super().__init__(manufacture.product if manufacture else product)
        self.manufacture = manufacture

    def all_states(self):
        return Manufacture.STATUS

    def manufacture(self):
        return self.manufacture

    def selected_status(self):
        return self.manufacture.status if self.manufacture else ''

    def selected_size(self):
        return self.manufacture.size if self.manufacture else 0

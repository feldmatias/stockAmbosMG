from Products.decorators.product_bar_decorator import ProductBarDecorator
from Stock.models import Stock


class ProductStockDecorator(ProductBarDecorator):
    def __init__(self, product):
        super().__init__(product)
        self.stock = self._initialize_stock()

    def stock(self):
        return self.stock

    def _initialize_stock(self):
        stock = {}
        if not self.product:
            return stock

        for color in self.product.colors:
            sizes = {}
            for size in self.product.sizes:
                sizes[size] = Stock.repository.find_or_create(color, size)
            stock[color] = sizes
        return stock
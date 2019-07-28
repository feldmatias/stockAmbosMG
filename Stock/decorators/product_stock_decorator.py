from Products.models import Product
from Stock.models import Stock


class ProductStockDecorator:
    def __init__(self, product):
        self.product = product
        self.stock = self._initialize_stock()

    def all_products(self):
        return Product.objects.all().order_by('id')

    def product(self):
        return self.product

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

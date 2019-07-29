from Stock.models import Stock


class ProductStockPresenter:
    def __init__(self, product):
        self.product = product
        self.stock = self._initialize_stock()

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

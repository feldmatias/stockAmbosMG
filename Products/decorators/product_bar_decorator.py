from Products.models import Product


class ProductBarDecorator:
    def __init__(self, product):
        self.product = product

    def all_products(self):
        return Product.objects.all().order_by('id')

    def product(self):
        return self.product

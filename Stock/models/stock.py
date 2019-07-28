from django.db import models

from Products.models import ProductColor, ProductSize
from Stock.managers.stock_manager import StockManager


class Stock(models.Model):
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    repository = StockManager()

    def update_stock(self, new_stock):
        self.stock = new_stock
        if self.stock < 0:
            self.stock = 0
        self.save()

    def add_stock(self, amount):
        self.update_stock(self.stock + amount)
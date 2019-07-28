from django.db import models

from Stock.models import stock as model
from Stock.validators.stock_validator import StockValidator


class StockManager(models.Manager):

    def create(self, color, size):
        StockValidator.validate(color, size)
        stock = model.Stock(color=color, size=size, stock=0)
        stock.save()
        return stock

    def find_or_create(self, color, size):
        stock = self.filter(color=color, size=size).first()
        return stock if stock is not None else self.create(color, size)

    def update_stock_from_manufacture(self, manufacture):
        for item in manufacture.items():
            stock = self.find_or_create(item.color, manufacture.size)
            stock.add_stock(item.count)

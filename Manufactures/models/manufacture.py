from django.db import models
from model_utils import Choices
from model_utils.models import StatusModel

from Manufactures.managers import ManufactureManager
from Products.models import ProductSize, Product
from Stock.models import Stock


class Manufacture(StatusModel):
    STATUS_PREPARATION = 'para_preparar'
    STATUS_CUT = 'cortados'
    STATUS_SEWING = 'en_costura'

    STATUS = Choices(
        (STATUS_PREPARATION, 'Para preparar'),
        (STATUS_CUT, 'Cortados'),
        (STATUS_SEWING, 'En costura')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)

    repository = ManufactureManager()

    def items(self):
        return self.manufactureitem_set.all()

    def next_status(self):
        if self.status == Manufacture.STATUS_PREPARATION:
            self.to_status(Manufacture.STATUS_CUT)

        elif self.status == Manufacture.STATUS_CUT:
            self.to_status(Manufacture.STATUS_SEWING)

        elif self.status == Manufacture.STATUS_SEWING:
            self.finish()

    def to_status(self, new_status):
        self.status = new_status
        self.save()

    def finish(self):
        Stock.repository.update_stock_from_manufacture(self)
        self.delete()

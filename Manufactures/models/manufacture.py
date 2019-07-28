from datetime import date

from django.db import models

from Manufactures.managers import ManufactureManager
from Products.models import ProductSize, Product
from Stock.models import Stock


class Manufacture(models.Model):
    STATE_PREPARATION = 'para_preparar'
    STATE_CUT = 'cortados'
    STATE_SEWING = 'en_costura'

    STATES = [
        (STATE_PREPARATION, 'Para preparar'),
        (STATE_CUT, 'Cortados'),
        (STATE_SEWING, 'En costura')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=STATES, default=STATE_PREPARATION)
    updated_at = models.DateField(auto_now_add=True)

    repository = ManufactureManager()

    def items(self):
        return self.manufactureitem_set.all()

    def next_state(self):
        if self.state == Manufacture.STATE_PREPARATION:
            self.to_state(Manufacture.STATE_CUT)
        elif self.state == Manufacture.STATE_CUT:
            self.to_state(Manufacture.STATE_SEWING)
        elif self.state == Manufacture.STATE_SEWING:
            self.finish()

    def to_state(self, new_state):
        self.state = new_state
        self.updated_at = date.today()
        self.save()

    def finish(self):
        Stock.repository.update_stock_from_manufacture(self)
        self.delete()

from django.db import models
from model_utils import Choices

from Sales.managers.SaleManager import SaleManager


class Sale(models.Model):
    TYPE_SALE = 'venta'
    TYPE_WITHDRAWAL = 'retiro'

    TYPES = Choices(
        (TYPE_SALE, 'Venta'),
        (TYPE_WITHDRAWAL, 'Retiro'),
    )

    value = models.IntegerField()
    date = models.DateField(auto_now=True)
    type = models.CharField(max_length=255, choices=TYPES)

    objects = SaleManager()

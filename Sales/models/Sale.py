from django.db import models
from model_utils import Choices

from Sales.managers.SaleManager import SaleManager


class Sale(models.Model):

    TYPES = Choices(
        ('1', 'Prendas Correo'),
        ('2', 'Facturas Ventas'),
        ('3', 'Facturas Compras'),
        ('4', 'Liquidación Laura'),
        ('5', 'Liquidación Graciela'),
        ('6', 'Publicidad'),
        ('7', 'Gastos'),
        ('8', 'Impuestos'),
    )

    value = models.IntegerField()
    date = models.DateField(auto_now=False)
    type = models.CharField(max_length=255, choices=TYPES)

    objects = SaleManager()

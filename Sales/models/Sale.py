from django.db import models
from model_utils import Choices

from Sales.managers.SaleManager import SaleManager


class Sale(models.Model):

    TYPES = Choices(
        ('1', 'Prendas Correo'),
        ('2', 'Prendas Malabia'),
        ('3', 'Banco Luli'),
        ('4', 'Semana Luli'),
        ('5', 'Retiros Dylan'),
        ('5', 'Banco Dylan'),
    )

    value = models.IntegerField()
    date = models.DateField(auto_now=False)
    type = models.CharField(max_length=255, choices=TYPES)

    objects = SaleManager()

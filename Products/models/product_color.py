from django.db import models

from Products.managers.ProductColorManager import ProductColorManager
from Products.models import Product


class ProductColor(models.Model):
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colores'

    color = models.CharField('color', max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = ProductColorManager()

    def __str__(self):
        return self.color

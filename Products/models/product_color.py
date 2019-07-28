from django.db import models

from Products.models import Product


class ProductColor(models.Model):
    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colores'

    color = models.CharField('color', max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.color

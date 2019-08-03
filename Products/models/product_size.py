from django.db import models

from Products.models import Product


class ProductSize(models.Model):
    class Meta:
        verbose_name = 'talle'
        verbose_name_plural = 'talles'

    DEFAULT_SIZE = '-'

    size = models.CharField('talle', max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.size

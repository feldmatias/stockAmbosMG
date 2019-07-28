from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    name = models.CharField('nombre', max_length=200)

    def __str__(self):
        return self.name

    @property
    def colors(self):
        return self.productcolor_set.all().order_by('id')

    @property
    def sizes(self):
        return self.productsize_set.all().order_by('id')

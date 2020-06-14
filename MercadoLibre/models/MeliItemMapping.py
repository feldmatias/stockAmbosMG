from django.db import models

from MercadoLibre.managers.MeliItemMappingManager import MeliItemMappingManager
from MercadoLibre.models import MeliItem
from Products.models import ProductColor, ProductSize


class MeliItemMapping(models.Model):
    item_id = models.CharField(max_length=255)
    meli_item = models.ForeignKey(MeliItem, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)

    objects = MeliItemMappingManager()

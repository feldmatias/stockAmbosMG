from django.db import models

from MercadoLibre.managers.MeliItemManager import MeliItemManager
from MercadoLibre.models import MeliUser
from Products.models import Product


class MeliItem(models.Model):
    item_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    meli_user = models.ForeignKey(MeliUser, on_delete=models.CASCADE)

    objects = MeliItemManager()

from django.db import models

from Manufactures.models import Manufacture
from Products.models import ProductColor


class ManufactureItem(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

from django.db import models

from Manufactures import models as model
from Manufactures.validators.manufacture_validator import ManufactureValidator


class ManufactureManager(models.Manager):

    def find_by_status(self, status):
        return self.filter(status=status).all().order_by('product_id', 'status_changed')

    def create_with_items(self, product, size, status, colors):
        ManufactureValidator.validate(product, size, colors)

        manufacture = self.create(product=product, size=size, status=status)
        self.set_manufacture_colors(manufacture, colors)

    def edit_with_items(self, manufacture, size, status, colors):
        ManufactureValidator.validate(manufacture.product, size, colors)

        manufacture.size = size
        manufacture.status = status
        manufacture.save()

        self.set_manufacture_colors(manufacture, colors)

    def set_manufacture_colors(self, manufacture, colors):
        manufacture.manufactureitem_set.all().delete()
        for color, value in colors.items():
            model.ManufactureItem.objects.create(color=color, count=value, manufacture=manufacture)

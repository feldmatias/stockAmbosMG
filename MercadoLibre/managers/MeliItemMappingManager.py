from django.db import models

from MercadoLibre.services.MeradoLibreService import MercadoLibreService
from Products.models import ProductSize, ProductColor


class MeliItemMappingManager(models.Manager):

    def find_for(self, item, size, color):
        return self.filter(meli_item=item, color=color, size=size).first()

    def automatic_mapping(self, meli_item):
        if not meli_item.product:
            self.filter(meli_item=meli_item).delete()
            return

        variations = MercadoLibreService().get_item_variations(meli_item)
        if not variations:
            return

        self.filter(meli_item=meli_item).delete()

        for variation in variations:
            size = ProductSize.objects.find_by_name_and_product(variation['size'], meli_item.product)
            color = ProductColor.objects.find_by_name_and_product(variation['color'], meli_item.product)

            if color and size:
                self.create(item_id=variation['id'], meli_item=meli_item, color=color, size=size)

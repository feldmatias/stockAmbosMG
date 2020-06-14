from django.db import models


class MeliItemManager(models.Manager):

    def find_or_create(self, meli_user, item_id):
        item, _ = self.get_or_create(meli_user=meli_user, item_id=item_id)
        return item

    def set_item_product(self, user_id, item_id, product):
        self.filter(meli_user__id=user_id, item_id=item_id).update(product=product)

    def automatic_variations_mapping(self, meli_user_id):
        from MercadoLibre.models import MeliItemMapping
        items = self.filter(meli_user__id=meli_user_id)
        for item in items:
            MeliItemMapping.objects.automatic_mapping(item)

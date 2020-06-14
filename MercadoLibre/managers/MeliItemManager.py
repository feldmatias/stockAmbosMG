from django.db import models


class MeliItemManager(models.Manager):

    def find_or_create(self, meli_user, item_id):
        item, _ = self.get_or_create(meli_user=meli_user, item_id=item_id)
        return item

    def set_item_product(self, user_id, item_id, product):
        self.filter(meli_user__id=user_id, item_id=item_id).update(product=product)

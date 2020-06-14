from django.db import models


class MeliItemManager(models.Manager):

    def find_or_create(self, meli_user, item_id):
        item, _ = self.get_or_create(meli_user=meli_user, item_id=item_id)
        return item

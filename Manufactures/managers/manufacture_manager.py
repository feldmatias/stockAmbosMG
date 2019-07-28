from django.db import models


class ManufactureManager(models.Manager):

    def find_by_state(self, state):
        return self.filter(state=state).all().order_by('product_id', 'updated_at')

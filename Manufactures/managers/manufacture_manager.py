from django.db import models


class ManufactureManager(models.Manager):

    def find_by_status(self, status):
        return self.filter(status=status).all().order_by('product_id', 'status_changed')

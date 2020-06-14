from django.db import models


class ProductColorManager(models.Manager):

    def find_by_name_and_product(self, name, product):
        return self.filter(color__iexact=name.lower(), product=product).first()

from django.db import models


class ProductSizeManager(models.Manager):

    def find_by_name_and_product(self, name, product):
        return self.filter(size__iexact=name.lower(), product=product).first()

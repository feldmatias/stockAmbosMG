from django.db import models


class SaleManager(models.Manager):

    def for_month(self, month, year):
        return self.filter(date__year=year, date__month=month).all()

    def create_with_value(self, sale_type, value, date):
        return self.create(type=sale_type, value=value, date=date)

from collections import OrderedDict

from django.utils import timezone


class SalesPresenter:

    def __init__(self, sales, month, year):
        self.all_sales = sales
        self.month = month
        self.year = year
        self.calculate_sales_per_day()
        self.calculate_totals()

    def calculate_totals(self):
        totals = {}
        for sales in self.sales.values():
            for type, value in sales.items():
                total = totals.get(type, 0)
                total += value
                totals[type] = total
        self.totals = totals

    @property
    def years(self):
        return list(range(2020, timezone.now().year + 1))

    def calculate_sales_per_day(self):
        sales = OrderedDict()
        for sale in self.all_sales.order_by('date'):
            day_sales = sales.get(sale.date.day, {})
            day_sales[sale.type] = sale.value
            sales[sale.date.day] = day_sales
        self.sales = sales

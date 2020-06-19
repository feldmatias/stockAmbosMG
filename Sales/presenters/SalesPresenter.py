from django.utils import timezone


class SalesPresenter:

    def __init__(self, sales, month, year):
        self.sales = sales
        self.month = month
        self.year = year
        self.calculate_totals()

    def calculate_totals(self):
        totals = {}
        for sale in self.sales:
            total = totals.get(sale.type, 0)
            total += sale.value
            totals[sale.type] = total
        self.totals = totals

    @property
    def years(self):
        return list(range(2020, timezone.now().year + 1))

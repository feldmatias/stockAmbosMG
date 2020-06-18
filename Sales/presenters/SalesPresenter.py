class SalesPresenter:

    def __init__(self, sales):
        self.sales = sales
        self.calculate_totals()

    def calculate_totals(self):
        totals = {}
        for sale in self.sales:
            total = totals.get(sale.type, 0)
            total += sale.value
            totals[sale.type] = total
        self.totals = totals

import threading

from Stock.models import Stock


class StockService:

    def update_stock(self, stock_id, new_stock):
        stock = Stock.repository.get(pk=stock_id)
        stock.update_stock(new_stock)
        self._update_stock(stock)

    def update_stock_from_manufacture(self, manufacture):
        for item in manufacture.items():
            stock = Stock.repository.find_or_create(item.color, manufacture.size)
            stock.add_stock(item.count)
            self._update_stock(stock)

    def _update_stock(self, stock):
        """ Update stock at MercadoLibre in a thread """
        thread = threading.Thread(target=update_stock_meli, args=[stock])
        thread.setDaemon(True)
        thread.start()


def update_stock_meli(stock):
    from MercadoLibre.services.MeradoLibreService import MercadoLibreService
    MercadoLibreService().update_stock(stock)

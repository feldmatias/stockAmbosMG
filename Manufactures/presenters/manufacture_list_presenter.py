from Manufactures.models import Manufacture
from Products.presenters.product_bar_presenter import ProductBarPresenter


class ManufactureListPresenter(ProductBarPresenter):
    def __init__(self, state):
        super().__init__()
        self.state = state
        self._initialize_manufactures()

    def all_states(self):
        return Manufacture.STATUS

    def state(self):
        return self.state

    def manufactures(self):
        return self.manufactures

    def _initialize_manufactures(self):
        self.manufactures = Manufacture.repository.find_by_status(self.state) if self.state else []

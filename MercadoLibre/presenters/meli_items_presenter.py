from MercadoLibre.models import MeliItem
from MercadoLibre.services.MeradoLibreService import MercadoLibreService


class MapMeliItemsPresenter:

    def __init__(self, meli_user):
        self.user = meli_user
        self.meli_items = MercadoLibreService().get_items(meli_user)
        self.initialize_items()

    def initialize_items(self):
        items = {}
        for item in self.meli_items:
            items[item] = MeliItem.objects.find_or_create(item_id=item, meli_user=self.user)
        self.all_items = items

    def user(self):
        return self.user

    def item_ids(self):
        return self.meli_items

    def items(self):
        return self.all_items

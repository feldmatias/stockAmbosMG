from MercadoLibre.models import MeliItemMapping
from MercadoLibre.services.MeradoLibreService import MercadoLibreService


class MeliMissingMappingsPresenter:

    def __init__(self, meli_user):
        self.user = meli_user
        self.items = meli_user.items
        self.initialize_missing_mappings()

    def initialize_missing_mappings(self):
        missing = []
        for item in self.items:
            if not item.product:
                continue

            title = MercadoLibreService().get_item_title(self.user, item.item_id)

            for size in item.product.sizes:
                for color in item.product.colors:
                    mapping = MeliItemMapping.objects.find_for(item, size, color)
                    if not mapping:
                        missing.append({
                            'item': title,
                            'size': size.size,
                            'color': color.color,
                        })
        self.missing = missing

    def missing_mappings(self):
        return self.missing

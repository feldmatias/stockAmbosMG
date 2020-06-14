from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from MercadoLibre.models import MeliUser, MeliItem
from MercadoLibre.presenters.meli_items_presenter import MapMeliItemsPresenter
from Products.models import Product

ITEM_NAME = 'item-'


class MapMeliItemsView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        meli_user = MeliUser.objects.get(pk=user_id)

        data = {
            'data': MapMeliItemsPresenter(meli_user)
        }

        return render(request, 'mercadolibre/map_items.html', data)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        for key, value in request.POST.items():
            if ITEM_NAME in key:
                item_id = key.lstrip(ITEM_NAME)
                product = get_object_or_404(Product, pk=value) if int(value) else None
                MeliItem.objects.set_item_product(user_id, item_id, product)

        MeliItem.objects.automatic_variations_mapping(user_id)

        messages.success(request, 'Publicaciones mapeadas correctamente')
        return redirect('mercadolibre:index')

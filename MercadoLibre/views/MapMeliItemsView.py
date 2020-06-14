from django.shortcuts import render
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.presenters.meli_items_presenter import MapMeliItemsPresenter


class MapMeliItemsView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        meli_user = MeliUser.objects.get(pk=user_id)

        data = {
            'data': MapMeliItemsPresenter(meli_user)
        }

        return render(request, 'mercadolibre/map_items.html', data)

    def post(self, request, *args, **kwargs):
        pass
from django.shortcuts import render
from django.views import View

from MercadoLibre.models import MeliItemMapping
from MercadoLibre.presenters.meli_user_list_presenter import MeliUsersListPresenter


class MeliIndexView(View):

    def get(self, request, *args, **kwargs):
        a = MeliItemMapping.objects.all()

        data = {
            'data': MeliUsersListPresenter()
        }

        return render(request, 'mercadolibre/index.html', data)

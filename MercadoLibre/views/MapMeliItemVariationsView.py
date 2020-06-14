from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.presenters.meli_missing_mappings_presenter import MeliMissingMappingsPresenter


class MapMeliItemVariationsView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        meli_user = MeliUser.objects.get(pk=user_id)

        data = {
            'data': MeliMissingMappingsPresenter(meli_user)
        }

        return render(request, 'mercadolibre/map_item_variations.html', data)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        MeliUser.objects.automatic_variations_mapping(user_id)

        messages.success(request, 'Talles y colores mapeados correctamente')
        return redirect(reverse('mercadolibre:map_item_variations', kwargs={'user_id': user_id}))

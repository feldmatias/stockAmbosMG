from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.presenters.meli_missing_mappings_presenter import MeliMissingMappingsPresenter
from MercadoLibre.services.MeradoLibreService import MercadoLibreService


class UpdateMeliStockView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        meli_user = MeliUser.objects.get(pk=user_id)
        
        MercadoLibreService().update_user_stock(meli_user)

        messages.success(request, 'Stock actualizado con éxito')

        return redirect('mercadolibre:index')


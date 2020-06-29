from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.presenters.meli_missing_mappings_presenter import MeliMissingMappingsPresenter
from Stock.services.StockService import StockService


class UpdateMeliStockView(View):

    def get(self, request, *args, **kwargs):
        StockService().update_all_stocks()

        messages.success(request, 'Stock actualizado con éxito')

        return redirect('mercadolibre:index')


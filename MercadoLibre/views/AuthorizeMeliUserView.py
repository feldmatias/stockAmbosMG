from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.services.MeradoLibreService import MercadoLibreService


class AuthorizeMeliUserView(View):

    def get(self, request, *args, **kwargs):
        authorization_code = request.GET.get('code')
        redirect_url = request.build_absolute_uri(reverse('mercadolibre:authorize_user'))

        meli_user = MeliUser.objects.for_authorization()
        authorized = MercadoLibreService().authorize_user(meli_user, authorization_code, redirect_url)

        if authorized:
            messages.success(request, 'Usuario de Mercado Libre asociado con éxito')
        else:
            messages.error(request, 'Ocurrió un error al comunicarse con Mercado Libre')

        return redirect('mercadolibre:index')

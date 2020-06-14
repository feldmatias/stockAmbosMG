from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from MercadoLibre.models import MeliUser
from MercadoLibre.services.MeradoLibreService import MercadoLibreService


class CreateMeliUserView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mercadolibre/create_user.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        client_id = request.POST.get('clientId')
        client_secret = request.POST.get('clientSecret')

        user = MeliUser.objects.create_user(name, client_id, client_secret)
        redirect_url = request.build_absolute_uri(reverse('mercadolibre:authorize_user'))

        return redirect(MercadoLibreService().get_authorization_url(user, redirect_url))

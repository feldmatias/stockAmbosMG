from django.shortcuts import render, redirect
from django.views import View

from MercadoLibre.models import MeliUser


class CreateMeliUserView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mercadolibre/create_user.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        app_id = request.POST.get('appId')
        client_id = request.POST.get('clientId')

        MeliUser.objects.create_user(name, app_id, client_id)

        return redirect('mercadolibre:index')

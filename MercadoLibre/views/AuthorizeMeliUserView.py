from django.shortcuts import render
from django.views import View


class AuthorizeMeliUserView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mercadolibre/create_user.html')

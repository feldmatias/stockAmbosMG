from django.shortcuts import render
from django.views import View


class MeliIndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mercadolibre/index.html')
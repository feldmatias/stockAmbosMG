from django.shortcuts import render
from django.views import View


class ConfigView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'config/index.html')

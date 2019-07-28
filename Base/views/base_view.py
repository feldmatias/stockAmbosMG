from django.shortcuts import redirect
from django.views import View


class BaseView(View):

    def get(self, request, *args, **kwargs):
        return redirect('stock:index')

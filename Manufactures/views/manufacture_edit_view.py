from django.shortcuts import render, get_object_or_404
from django.views import View

from Manufactures.models import Manufacture
from Manufactures.presenters.manufacture_presenter import ManufacturePresenter


class ManufactureEditView(View):

    def get(self, request, *args, **kwargs):
        manufacture_id = kwargs.get('id', 0)
        manufacture = get_object_or_404(Manufacture, pk=manufacture_id)

        data = {
            'data': ManufacturePresenter(manufacture=manufacture)
        }

        return render(request, 'manufacture/create.html', data)

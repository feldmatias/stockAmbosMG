from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Manufactures.decorators.manufacture_decorator import ManufactureDecorator
from Manufactures.models import Manufacture
from Products.models import Product, ProductSize, ProductColor


class ManufactureEditView(View):

    def get(self, request, *args, **kwargs):
        manufacture_id = kwargs.get('id', 0)
        manufacture = get_object_or_404(Manufacture, pk=manufacture_id)

        data = {
            'data': ManufactureDecorator(manufacture=manufacture)
        }

        return render(request, 'manufacture/create.html', data)


from django.shortcuts import render
from django.views import View

from Manufactures.decorators.manufacture_list_decorator import ManufactureListDecorator


class ManufactureListView(View):

    def get(self, request, *args, **kwargs):
        state = kwargs.get('state')

        data = {
            'data': ManufactureListDecorator(state)
        }

        return render(request, 'manufacture/list.html', data)

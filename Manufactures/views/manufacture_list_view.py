from django.shortcuts import render
from django.views import View

from Manufactures.presenters.manufacture_list_presenter import ManufactureListPresenter


class ManufactureListView(View):

    def get(self, request, *args, **kwargs):
        state = kwargs.get('state')

        data = {
            'data': ManufactureListPresenter(state)
        }

        return render(request, 'manufacture/list.html', data)

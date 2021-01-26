from django.contrib import messages
from django.shortcuts import redirect

from Manufactures.views.manufacture_crud_base_view import ManufactureCrudBaseView


class ManufactureDeleteView(ManufactureCrudBaseView):

    def post(self, request, *args, **kwargs):
        self.manufacture.delete()
        messages.success(request, 'Pedido eliminado con éxito')
        return redirect('manufactures:list', state=self.current_status)

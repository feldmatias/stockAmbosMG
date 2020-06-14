from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from MercadoLibre.models import MeliUser


class DeleteMeliUserView(View):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(MeliUser, pk=user_id)

        user.delete()
        messages.success(request, 'Usuario eliminado con éxito')

        return redirect('mercadolibre:index')

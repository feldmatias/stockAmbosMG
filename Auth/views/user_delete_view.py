from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views import View


class UserDeleteView(View):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(User, pk=user_id)

        if User.objects.count() <= 1:
            messages.error(request, 'No se puede eliminar al único usuario')
        else:
            user.delete()
            messages.success(request, 'Usuario eliminado con éxito')

        return redirect('users:config')

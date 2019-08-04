from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'users/create.html'
    success_message = "Usuario creado"
    success_url = reverse_lazy('users:config')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        return super().form_valid(form)

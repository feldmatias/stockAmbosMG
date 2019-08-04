from django.contrib.auth.models import User
from django.views.generic import ListView


class UserConfigListView(ListView):
    template_name = 'users/config_list.html'
    model = User
    context_object_name = 'users'
    ordering = ['id']

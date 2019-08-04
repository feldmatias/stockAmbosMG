from django.urls import path

from Auth.views.user_config_list_view import UserConfigListView
from Auth.views.user_create_view import UserCreateView
from Auth.views.user_delete_view import UserDeleteView

app_name = 'users'

urlpatterns = [
    path('configuracion', UserConfigListView.as_view(), name='config'),
    path('configuracion/crear', UserCreateView.as_view(), name='create'),
    path('configuracion/eliminar/<int:id>', UserDeleteView.as_view(), name='delete'),
]

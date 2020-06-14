from django.urls import path

from MercadoLibre.views.AuthorizeMeliUserView import AuthorizeMeliUserView
from MercadoLibre.views.CreateMeliUserView import CreateMeliUserView
from MercadoLibre.views.MeliIndexView import MeliIndexView

app_name = 'mercadolibre'

urlpatterns = [
    path('', MeliIndexView.as_view(), name='index'),
    path('usuarios/nuevo/', CreateMeliUserView.as_view(), name='create_user'),
    path('usuarios/autorizar/', AuthorizeMeliUserView.as_view(), name='authorize_user'),
]

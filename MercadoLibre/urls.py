from django.urls import path

from MercadoLibre.views.MeliIndexView import MeliIndexView

app_name = 'mercadolibre'

urlpatterns = [
    path('', MeliIndexView.as_view(), name='index'),
    path('usuarios/nuevo/', MeliIndexView.as_view(), name='create_user'),
]

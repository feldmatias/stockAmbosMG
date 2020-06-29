from django.urls import path

from MercadoLibre.views.AuthorizeMeliUserView import AuthorizeMeliUserView
from MercadoLibre.views.CreateMeliUserView import CreateMeliUserView
from MercadoLibre.views.DeleteMeliUserView import DeleteMeliUserView
from MercadoLibre.views.MapMeliItemVariationsView import MapMeliItemVariationsView
from MercadoLibre.views.MapMeliItemsView import MapMeliItemsView
from MercadoLibre.views.MeliIndexView import MeliIndexView
from MercadoLibre.views.UpdateMelIStockView import UpdateMeliStockView

app_name = 'mercadolibre'

urlpatterns = [
    path('', MeliIndexView.as_view(), name='index'),
    path('usuarios/nuevo/', CreateMeliUserView.as_view(), name='create_user'),
    path('usuarios/autorizar/', AuthorizeMeliUserView.as_view(), name='authorize_user'),
    path('usuarios/eliminar/<int:id>', DeleteMeliUserView.as_view(), name='delete_user'),
    path('publicaciones/mapear/<int:user_id>', MapMeliItemsView.as_view(), name='map_items'),
    path('publicaciones/mapear_talles_colores/<int:user_id>', MapMeliItemVariationsView.as_view(), name='map_item_variations'),
    path('publicaciones/actualizar_stock/', UpdateMeliStockView.as_view(), name='update_stock'),
]

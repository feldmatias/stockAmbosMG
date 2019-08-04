from django.urls import path

from Products.views.product_config_list_view import ProductConfigListView
from Products.views.product_create_view import ProductCreateView
from Products.views.product_delete_view import ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('configuracion', ProductConfigListView.as_view(), name='config'),
    path('configuracion/crear', ProductCreateView.as_view(), name='create'),
    path('configuracion/eliminar/<int:id>', ProductDeleteView.as_view(), name='delete'),
]

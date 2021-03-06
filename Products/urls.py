from django.urls import path

from Products.views.product_config_list_view import ProductConfigListView
from Products.views.product_create_view import ProductCreateView
from Products.views.product_delete_view import ProductDeleteView
from Products.views.product_edit_view import ProductEditView

app_name = 'products'

urlpatterns = [
    path('configuracion', ProductConfigListView.as_view(), name='config'),
    path('configuracion/crear', ProductCreateView.as_view(), name='create'),
    path('configuracion/editar/<int:pk>', ProductEditView.as_view(), name='edit'),
    path('configuracion/eliminar/<int:id>', ProductDeleteView.as_view(), name='delete'),
]

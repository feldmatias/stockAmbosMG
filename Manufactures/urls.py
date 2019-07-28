from django.urls import path

from Manufactures.views.manufacture_create_view import ManufactureCreateView
from Manufactures.views.manufacture_list_view import ManufactureListView
from Manufactures.views.manufacture_delete_view import ManufactureDeleteView
from Manufactures.views.manufacture_next_state_view import ManufactureNextStateView

app_name = 'manufactures'

urlpatterns = [
    path('', ManufactureListView.as_view(), name='index'),
    path('listado/<str:state>', ManufactureListView.as_view(), name='list'),
    path('<int:id>/delete', ManufactureDeleteView.as_view(), name='delete'),
    path('<int:id>/state/next', ManufactureNextStateView.as_view(), name='next-state'),
    path('crear', ManufactureCreateView.as_view(), name='create'),
    path('crear/<int:id>', ManufactureCreateView.as_view(), name='create-product'),
]

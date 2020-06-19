from django.urls import path

from Sales.views.SalesView import SalesView

app_name = 'sales'

urlpatterns = [
    path('', SalesView.as_view(), name='index'),
]

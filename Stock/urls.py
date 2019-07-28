from django.urls import path

from Stock.views.stock_view import StockView

app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name='index'),
    path('<int:id>', StockView.as_view(), name='stock')
]

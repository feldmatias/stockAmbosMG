from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Products.models import Product
from Stock.presenters.product_stock_presenter import ProductStockPresenter
from Stock.models import Stock

STOCK_NAME = 'stock-'


class StockView(View):

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id', 0)
        editable = request.GET.get('editable', False)

        product = get_object_or_404(Product, pk=product_id) if product_id != 0 else None

        data = {
            'data': ProductStockPresenter(product),
            'editable': editable
        }
        return render(request, 'stock/index.html', data)

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        for key, value in request.POST.items():
            if STOCK_NAME in key:
                stock_id = key.lstrip(STOCK_NAME)
                stock = Stock.repository.get(pk=stock_id)
                stock.update_stock(int(value))

        messages.success(request, 'Stock actualizado')
        return redirect('stock:stock', id=product_id)

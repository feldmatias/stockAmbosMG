from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from Products.models import Product


class ProductDeleteView(View):

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Producto eliminado con éxito')
        return redirect('products:config')

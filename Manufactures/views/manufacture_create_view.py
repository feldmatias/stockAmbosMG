from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Manufactures.decorators.manufacture_decorator import ManufactureDecorator
from Manufactures.models import Manufacture
from Products.models import Product, ProductSize, ProductColor

COLOR_NAME = 'color-'


class ManufactureCreateView(View):

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id', 0)
        product = get_object_or_404(Product, pk=product_id) if product_id != 0 else None

        data = {
            'data': ManufactureDecorator(product=product)
        }

        return render(request, 'manufacture/create.html', data)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('id'))
        size = get_object_or_404(ProductSize, pk=request.POST.get('product-size'))
        status = request.POST.get('status')

        colors = {}
        for key, value in request.POST.items():
            if COLOR_NAME in key:
                color_id = key.lstrip(COLOR_NAME)
                color = get_object_or_404(ProductColor, pk=color_id)
                color_value = int(value)
                if color_value:
                    colors[color] = color_value

        Manufacture.repository.create_with_items(product, size, status, colors)

        return redirect('manufactures:list', state=status)

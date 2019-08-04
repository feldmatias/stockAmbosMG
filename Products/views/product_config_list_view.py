from django.views.generic import ListView

from Products.models import Product


class ProductConfigListView(ListView):
    template_name = 'products/config_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['id']

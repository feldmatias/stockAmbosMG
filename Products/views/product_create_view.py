from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView

from Products.forms.product_color_inline_formset import ProductColorInlineFormset
from Products.forms.product_size_inline_formset import ProductSizeInlineFormset
from Products.models import Product


class ProductCreateView(SuccessMessageMixin, CreateWithInlinesView):
    model = Product
    inlines = [ProductSizeInlineFormset, ProductColorInlineFormset]
    fields = ['name']
    template_name = 'products/create.html'
    success_message = "Producto creado"
    success_url = reverse_lazy('products:config')

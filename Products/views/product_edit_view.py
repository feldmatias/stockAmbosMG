from django.urls import reverse_lazy
from extra_views import UpdateWithInlinesView

from Base.mixins.FormsetSuccessMessageMixin import FormsetSuccessMessageMixin
from Products.forms.product_color_inline_formset import ProductColorInlineFormset
from Products.forms.product_size_inline_formset import ProductSizeInlineFormset
from Products.models import Product


class ProductEditView(FormsetSuccessMessageMixin, UpdateWithInlinesView):
    model = Product
    inlines = [ProductSizeInlineFormset, ProductColorInlineFormset]
    fields = ['name']
    template_name = 'products/create.html'
    success_message = "Producto editado"
    success_url = reverse_lazy('products:config')

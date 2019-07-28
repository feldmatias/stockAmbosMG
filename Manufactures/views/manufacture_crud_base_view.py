from django.shortcuts import get_object_or_404
from django.views import View

from Manufactures.models import Manufacture


class ManufactureCrudBaseView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, args, kwargs)

        manufacture_id = kwargs.get('id')
        self.manufacture = get_object_or_404(Manufacture, pk=manufacture_id)
        self.current_state = self.manufacture.state

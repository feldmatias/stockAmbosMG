from django.shortcuts import redirect

from Manufactures.views.manufacture_crud_base_view import ManufactureCrudBaseView


class ManufactureNextStateView(ManufactureCrudBaseView):

    def post(self, request, *args, **kwargs):
        self.manufacture.next_status()
        return redirect('manufactures:list', state=self.current_status)

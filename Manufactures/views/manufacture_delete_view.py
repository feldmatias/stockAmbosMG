from django.shortcuts import redirect

from Manufactures.views.manufacture_crud_base_view import ManufactureCrudBaseView


class ManufactureDeleteView(ManufactureCrudBaseView):

    def post(self, request, *args, **kwargs):
        self.manufacture.delete()
        return redirect('manufactures:list', state=self.current_status)

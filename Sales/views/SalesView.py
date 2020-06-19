from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from Sales.models import Sale
from Sales.presenters.SalesPresenter import SalesPresenter


class SalesView(View):

    def get(self, request, *args, **kwargs):
        month = request.GET.get('mes')
        year = request.GET.get('año')

        if not month or not year:
            now = timezone.now()
            month = now.month
            year = now.year

        sales = Sale.objects.for_month(int(month), int(year))

        data = {
            'data': SalesPresenter(sales, int(month), int(year))
        }
        return render(request, 'sales/index.html', data)

    def post(self, request, *args, **kwargs):
        sale_type = request.POST.get('type')
        value = request.POST.get('value')
        date = request.POST.get('date')

        Sale.objects.create_with_value(sale_type, value, date)

        return redirect('sales:index')

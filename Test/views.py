import json

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from Test.models import MeliEvent


@method_decorator(csrf_exempt, name='dispatch')
class MeliNotificationsView(View):

    def get(self, request, *args, **kwargs):
        events = MeliEvent.objects.all()
        return render(request, 'test/config_list.html', {'events': events})


    def post(self, request, *args, **kwargs):
        data = str(request.body)
        MeliEvent.objects.create(data=data)
        return HttpResponse(status=200)

from django.urls import path

from Config.views.config_view import ConfigView

app_name = 'config'

urlpatterns = [
    path('', ConfigView.as_view(), name='index')
]

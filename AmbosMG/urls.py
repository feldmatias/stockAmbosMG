"""AmbosMG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from Base.views.base_view import BaseView

urlpatterns = [
    path('stock/', include('Stock.urls', namespace='stock')),
    path('cortes/', include('Manufactures.urls', namespace='manufactures')),
    path('productos/', include('Products.urls', namespace='products')),
    path('mercadolibre/', include('MercadoLibre.urls', namespace='mercadolibre')),
    path('configuracion/', include('Config.urls', namespace='config')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('Auth.urls', namespace='users')),
    path('', BaseView.as_view(), name='default'),
]

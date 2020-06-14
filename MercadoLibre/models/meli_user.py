from datetime import datetime, timedelta

from django.db import models

from MercadoLibre.managers.MeliUserManager import MeliUserManager


class MeliUser(models.Model):

    name = models.CharField(max_length=200)
    app_id = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)

    access_token = models.CharField(max_length=255, null=True)
    refresh_token = models.CharField(max_length=255, null=True)
    token_expiration = models.DateTimeField(null=True)
    token_updated = models.DateTimeField(null=True)

    objects = MeliUserManager()

    def __str__(self):
        return self.name

    def set_access_token(self, access_token, refresh_token, token_expires_in):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_updated = datetime.now()
        self.token_expiration = datetime.now() + timedelta(seconds=token_expires_in)
        self.save()

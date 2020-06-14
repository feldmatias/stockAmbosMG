from datetime import timedelta

from django.db import models
from django.utils import timezone

from MercadoLibre.managers.MeliUserManager import MeliUserManager


class MeliUser(models.Model):
    name = models.CharField(max_length=200)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)

    user_id = models.PositiveIntegerField(null=True)
    access_token = models.CharField(max_length=255, null=True)
    refresh_token = models.CharField(max_length=255, null=True)
    token_expiration = models.DateTimeField(null=True)

    objects = MeliUserManager()

    def __str__(self):
        return self.name

    def set_access_token(self, access_token, refresh_token, token_expires_in):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expiration = timezone.now() + timedelta(seconds=token_expires_in)
        self.save()

    def token_expired(self):
        return self.token_expiration <= timezone.now()

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.save()

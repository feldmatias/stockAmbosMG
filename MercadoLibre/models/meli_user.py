from django.db import models


class MeliUser(models.Model):

    name = models.CharField('nombre', max_length=200)
    client_id = models.IntegerField()
    app_id = models.IntegerField()

    access_token = models.CharField(max_length=255, null=True)
    refresh_token = models.CharField(max_length=255, null=True)
    token_expiration = models.DateTimeField(null=True)
    token_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

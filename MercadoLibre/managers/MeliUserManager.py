from django.db import models


class MeliUserManager(models.Manager):

    def create_user(self, name, client_id, client_secret):
        return self.create(name=name, client_id=client_id, client_secret=client_secret)

    def for_authorization(self):
        return self.filter(access_token__isnull=True).last()  # TODO: find a better way to identify the user to authorize

    def authorized(self):
        return self.filter(access_token__isnull=False)

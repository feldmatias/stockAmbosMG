from django.db import models


class MeliUserManager(models.Manager):

    def create_user(self, name, app_id, client_id):
        return self.create(name=name, app_id=app_id, client_id=client_id)

    def for_authorization(self):
        return self.filter(access_token__isnull=True).last()  # TODO: find a better way to identify the user to authorize

    def authorized(self):
        return self.filter(access_token__isnull=False)

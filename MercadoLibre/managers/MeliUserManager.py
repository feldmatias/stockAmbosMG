from django.db import models


class MeliUserManager(models.Manager):

    def create_user(self, name, app_id, client_id):
        return self.create(name=name, app_id=app_id, client_id=client_id)

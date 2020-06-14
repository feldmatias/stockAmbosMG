from django.db import models

# Create your models here.

class MeliEvent(models.Model):
    when = models.DateTimeField(auto_now=True)
    data = models.TextField()
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "Ambos MG"
admin.site.site_title = "Ambos MG"
admin.site.index_title = "Ambos MG"

admin.site.unregister(Group)

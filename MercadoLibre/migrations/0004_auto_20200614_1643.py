# Generated by Django 2.2.3 on 2020-06-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MercadoLibre', '0003_auto_20200614_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meliuser',
            old_name='client_id',
            new_name='client_secret',
        ),
    ]

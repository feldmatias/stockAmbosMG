# Generated by Django 2.2.3 on 2019-07-27 20:54

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Manufactures', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='manufacture',
            managers=[
                ('repository', django.db.models.manager.Manager()),
            ],
        ),
    ]

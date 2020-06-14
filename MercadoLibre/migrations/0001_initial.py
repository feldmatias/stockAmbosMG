# Generated by Django 2.2.3 on 2020-06-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeliUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('client_id', models.IntegerField()),
                ('app_id', models.IntegerField()),
                ('access_token', models.CharField(max_length=255, null=True)),
                ('refresh_token', models.CharField(max_length=255, null=True)),
                ('token_expiration', models.DateTimeField(null=True)),
                ('token_updated', models.DateTimeField(null=True)),
            ],
        ),
    ]

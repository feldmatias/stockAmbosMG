# Generated by Django 3.0.7 on 2020-06-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('1', 'Prendas Correo'), ('2', 'Prendas Malabia'), ('3', 'Retiros Luli'), ('4', 'Semana Luli'), ('5', 'Retiros Dylan'), ('5', 'Semana Dylan')], max_length=255),
        ),
    ]

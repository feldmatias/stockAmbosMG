# Generated by Django 3.0.7 on 2020-06-19 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0002_auto_20200618_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 2.2.3 on 2020-06-14 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20190720_2016'),
        ('MercadoLibre', '0005_auto_20200614_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeliItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('meli_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MercadoLibre.MeliUser')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.Product')),
            ],
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-27 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0002_auto_20190720_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('preparation', 'Para preparar'), ('cut', 'Cortado'), ('sewing', 'En costura')], default='preparation', max_length=50)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.ProductSize')),
            ],
        ),
        migrations.CreateModel(
            name='ManufactureItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.ProductColor')),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manufactures.Manufacture')),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2021-01-26 18:23

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Manufactures', '0007_auto_20210126_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacture',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='en_costura', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
    ]

# Generated by Django 5.0 on 2023-12-14 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 13, 23, 58, 0, 8349)),
        ),
    ]

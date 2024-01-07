# Generated by Django 5.0 on 2023-12-23 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 23, 11, 9, 32, 47353)),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='upload/product'),
        ),
    ]
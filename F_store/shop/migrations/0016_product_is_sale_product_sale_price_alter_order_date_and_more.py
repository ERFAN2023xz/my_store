# Generated by Django 5.0 on 2023-12-24 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_order_date_alter_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 24, 7, 14, 49, 250414)),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='upload/product/'),
        ),
    ]

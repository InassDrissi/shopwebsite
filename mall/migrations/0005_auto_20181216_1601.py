# Generated by Django 2.1.3 on 2018-12-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
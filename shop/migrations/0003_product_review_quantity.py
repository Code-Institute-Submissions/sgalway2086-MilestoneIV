# Generated by Django 3.2.9 on 2021-12-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review_quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]

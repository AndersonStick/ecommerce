# Generated by Django 3.1.7 on 2023-10-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20231004_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='compare_price',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]

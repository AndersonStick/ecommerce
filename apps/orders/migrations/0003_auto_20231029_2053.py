# Generated by Django 3.1.7 on 2023-10-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20231025_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_zip_code',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='state_province_region',
            field=models.CharField(default='Bogota', max_length=255),
        ),
    ]

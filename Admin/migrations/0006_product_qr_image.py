# Generated by Django 2.2.1 on 2020-11-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_auto_20201108_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qr_image',
            field=models.ImageField(blank=True, upload_to='QR'),
        ),
    ]

# Generated by Django 2.2 on 2020-02-24 11:59

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200224_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.upload_image_path),
        ),
    ]

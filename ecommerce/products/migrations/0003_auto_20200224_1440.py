# Generated by Django 2.2 on 2020-02-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
# Generated by Django 3.2.19 on 2023-07-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_has_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='extra_warranty',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='garage_check',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='history_check',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='premium_check',
            field=models.BooleanField(null=True),
        ),
    ]

# Generated by Django 3.2.19 on 2023-08-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_orderlineitem_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not reviewed'), (1, 'Reviewed')], default=0),  # noqa E501
        ),
    ]

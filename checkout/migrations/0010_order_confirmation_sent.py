# Generated by Django 3.2.19 on 2023-08-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirmation_sent',
            field=models.BooleanField(default=False),
        ),
    ]

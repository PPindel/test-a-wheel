# Generated by Django 3.2.19 on 2023-07-24 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='team_ad', to=settings.AUTH_USER_MODEL),  # noqa E501
        ),
    ]

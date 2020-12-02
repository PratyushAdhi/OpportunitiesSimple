# Generated by Django 3.1.2 on 2020-11-30 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0013_auto_20201129_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='user',
            field=models.ForeignKey(blank=True, default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]

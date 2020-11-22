# Generated by Django 3.1.2 on 2020-11-22 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0007_auto_20201121_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='partner_type',
            field=models.CharField(blank=True, choices=[('college', 'College'), ('organization', 'Organization'), ('individual', 'Individual'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20201122_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='business_id',
            field=models.ManyToManyField(blank=True, to='leads.Business'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='genre_id',
            field=models.ManyToManyField(blank=True, to='leads.Genre'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='language_id',
            field=models.ManyToManyField(blank=True, to='leads.Language'),
        ),
    ]

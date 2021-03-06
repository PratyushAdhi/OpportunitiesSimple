# Generated by Django 3.1.2 on 2020-12-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_auto_20201130_1856'),
        ('details', '0007_auto_20201130_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='genre_id',
            field=models.ManyToManyField(blank=True, related_name='details', to='leads.Genre'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='language_id',
            field=models.ManyToManyField(blank=True, related_name='details', to='leads.Language'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

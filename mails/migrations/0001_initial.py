# Generated by Django 3.1.2 on 2020-11-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('subject', models.CharField(max_length=120)),
                ('body', models.TextField()),
            ],
        ),
    ]
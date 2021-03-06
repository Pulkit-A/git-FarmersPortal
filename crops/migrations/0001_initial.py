# Generated by Django 3.1.4 on 2020-12-29 04:07

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('msp', models.FloatField()),
                ('stock', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/images'), upload_to='')),
            ],
        ),
    ]

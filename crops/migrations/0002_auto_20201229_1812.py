# Generated by Django 3.1.4 on 2020-12-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

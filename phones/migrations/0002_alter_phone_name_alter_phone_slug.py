# Generated by Django 4.2.14 on 2024-07-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

# Generated by Django 3.0.8 on 2021-01-23 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0004_auto_20210120_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='universe',
            name='pixelOutUni',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(512)]),
        ),
        migrations.AlterField(
            model_name='universe',
            name='universeNumber',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(512)]),
        ),
    ]

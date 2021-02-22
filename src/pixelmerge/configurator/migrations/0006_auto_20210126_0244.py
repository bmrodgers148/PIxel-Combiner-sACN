# Generated by Django 3.0.8 on 2021-01-26 02:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0005_auto_20210123_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixel',
            name='outputUniverse',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(255)]),
        ),
    ]

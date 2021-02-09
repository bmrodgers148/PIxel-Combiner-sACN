# Generated by Django 3.0.8 on 2021-01-14 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pixel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixelType', models.TextField()),
                ('inputUniverse', models.IntegerField()),
                ('inputAddress', models.IntegerField()),
                ('outputUniverse', models.IntegerField()),
                ('outputAddress', models.IntegerField()),
                ('fixtureNum', models.IntegerField()),
                ('pixelNum', models.IntegerField()),
            ],
        ),
    ]
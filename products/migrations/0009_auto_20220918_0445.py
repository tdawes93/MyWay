# Generated by Django 3.2 on 2022-09-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_tour_choose_location_tour_choose_multiple_locations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='tour',
            name='choose_location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='choose_multiple_locations',
            field=models.BooleanField(default=False),
        ),
    ]
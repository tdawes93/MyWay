# Generated by Django 4.0 on 2022-09-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_tour_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='name',
            field=models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default=0, max_length=30),
        ),
    ]
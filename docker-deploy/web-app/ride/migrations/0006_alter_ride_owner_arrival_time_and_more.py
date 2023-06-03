# Generated by Django 4.1.5 on 2023-02-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0005_remove_ride_owner_sharer_ride_owner_sharer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride_owner',
            name='arrival_time',
            field=models.DateTimeField(help_text='Format: 2023-02-23 12:00'),
        ),
        migrations.AlterField(
            model_name='ride_sharer',
            name='earliest_arrival_time',
            field=models.DateTimeField(help_text='Format: 2023-02-23 12:00'),
        ),
        migrations.AlterField(
            model_name='ride_sharer',
            name='latest_arrival_time',
            field=models.DateTimeField(help_text='Format: 2023-02-23 13:00'),
        ),
    ]
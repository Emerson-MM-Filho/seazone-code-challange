# Generated by Django 4.1.3 on 2022-11-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_rename_advertisement_id_booking_advertisement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guests_count',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_rename_property_id_advertisement_propriety'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

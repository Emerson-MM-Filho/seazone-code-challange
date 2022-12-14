# Generated by Django 4.1.3 on 2022-11-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propriety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activation_date', models.DateTimeField()),
                ('code', models.CharField(max_length=250, unique=True)),
                ('guests_limit', models.IntegerField()),
                ('bathroom_count', models.IntegerField()),
                ('pet_frendly', models.BooleanField()),
                ('cleaner_fee', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]

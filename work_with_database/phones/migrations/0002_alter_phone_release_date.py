# Generated by Django 5.1.1 on 2024-09-23 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 23, 13, 15, 18, 753179, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-28 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 28, 20, 3, 10, 213214, tzinfo=datetime.timezone.utc), max_length=50),
        ),
    ]

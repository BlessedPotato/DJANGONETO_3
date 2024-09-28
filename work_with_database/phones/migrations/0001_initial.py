# Generated by Django 5.1.1 on 2024-09-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.URLField()),
                ('release_date', models.DateField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
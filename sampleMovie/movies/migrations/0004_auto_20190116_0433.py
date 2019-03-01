# Generated by Django 2.1.5 on 2019-01-16 04:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_ratingpeliculas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='calificacion',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='ratingpeliculas',
            name='cali',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
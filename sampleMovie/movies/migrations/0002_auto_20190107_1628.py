# Generated by Django 2.1.5 on 2019-01-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoplan',
            name='costo',
            field=models.IntegerField(),
        ),
    ]

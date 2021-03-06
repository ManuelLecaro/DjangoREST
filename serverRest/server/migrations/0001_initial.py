# Generated by Django 2.1.5 on 2019-01-23 16:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('calificacion', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('reparto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RatingPeliculas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cali', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('pelicula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Peliculas')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.TipoPlan'),
        ),
        migrations.AddField(
            model_name='persona',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Plan'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Plan'),
        ),
        migrations.AddField(
            model_name='log',
            name='pelicula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Peliculas'),
        ),
        migrations.AddField(
            model_name='log',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Persona'),
        ),
    ]

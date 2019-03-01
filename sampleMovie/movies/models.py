from django.db import models
from django.db.models import Count
from django.db import connection 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models import Avg, Sum,F
# Create your models here.

class TipoPlan(models.Model):
	nombre = models.CharField(max_length=50)
	costo = models.IntegerField()

class Plan(models.Model):
	tipo = models.ForeignKey(TipoPlan,null=True,blank=True,on_delete=models.CASCADE)

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	fecha = models.DateField()
	user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	plan = models.ForeignKey(Plan,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellido)

class Peliculas(models.Model):
	titulo = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	calificacion = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
	plan = models.ForeignKey(Plan,null=True,blank=True,on_delete=models.CASCADE)
	reparto = models.TextField()
	def __str__(self):
		return '{}'.format(self.titulo)

	def peliculasList(idp):
		movie = Peliculas.objects.filter(id=idp).select_related('plan').annotate(peli=Count('id')).order_by('-plan')
		return movie

class Log(models.Model):
	fecha = models.DateField()
	usuario = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
	pelicula = models.ForeignKey(Peliculas,null=True,blank=True,on_delete=models.CASCADE)
	def top_n_peliculas(valor):
		movie = Log.objects.all().select_related('peliculas').annotate(peli=Count('pelicula_id')).order_by('-peli')[:valor]
		return movie

class RatingPeliculas(models.Model):
	pelicula = models.ForeignKey(Peliculas,null=True,blank=True,on_delete=models.CASCADE)
	persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
	cali=models.PositiveIntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
	def allpeliculas():
		peliculas= RatingPeliculas.objects.all().select_related('pelicula','persona').order_by('id')
		return peliculas

	def top_n_peliculas(valor):
		movie = Log.objects.all().select_related('pelicula').annotate(peli=Count('pelicula_id')).order_by('-peli')[:valor]
		return movie

	def peliculasCal(iduser):
		per = Persona.objects.get(user=iduser).id
		movie = RatingPeliculas.objects.filter(persona=per).select_related('pelicula')
		return movie

	def peliculasList(idp):
		movie = RatingPeliculas.objects.filter(pelicula=idp).annotate(calif=Sum('cali', distinct=True)).aggregate(Avg(F('calif')))
		return movie
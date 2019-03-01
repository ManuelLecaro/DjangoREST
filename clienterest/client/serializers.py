from rest_framework import serializers
from . import models

class TipoPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPlan
        fields = ('id', 'nombre',"costo")

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = ('id', 'tipo')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = ('id', 'nombre',"apellido","plan","fecha")

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Peliculas
        fields = ('id', 'titulo',"director","calificacion","plan","reparto")

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Log
        fields = ('id', 'fecha',"usuario","pelicula")

class RatingSerializer(serializers.ModelSerializer):
    #tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.RatingPeliculas
        fields = ('id', 'pelicula', 'persona','cali')#,'tracks')


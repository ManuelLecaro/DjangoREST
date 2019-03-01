from rest_framework import serializers
from server.models import TipoPlan, Plan, Peliculas, Persona, Log, RatingPeliculas

class TipoPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlan
        fields = ('id', 'nombre',"costo")

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'tipo')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombre',"apellido","plan","fecha")

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = ('id', 'titulo',"director","calificacion","plan","reparto")

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'fecha',"usuario","pelicula")

class RatingSerializer(serializers.ModelSerializer):
    #tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = RatingPeliculas
        fields = ('id', 'pelicula', 'persona','cali')#,'tracks')


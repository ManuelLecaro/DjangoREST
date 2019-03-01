from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from server.models import TipoPlan, Plan, Peliculas, Persona, Log, RatingPeliculas
from server.api.serializers import TipoPlanSerializer, PlanSerializer, PeliculasSerializer, PersonaSerializer, LogSerializer, RatingSerializer

class TipoPlanViewSet(viewsets.ModelViewSet):
    queryset = TipoPlan.objects.all()
    serializer_class = TipoPlanSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class RatingPeliculasViewSet(viewsets.ModelViewSet):
    queryset = RatingPeliculas.objects.all()
    serializer_class = RatingSerializer



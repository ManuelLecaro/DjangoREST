from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from serverRest.models import TipoPlan, Plan, Peliculas, Persona, Log, RatingPeliculas
from serverRest.api.serializers import TipoPlanSerializer, PlanSerializer, PeliculasSerializer, PersonaSerializer, LogSerializer, RatingSerializer

class TipoPlanListView(ListAPIView):
    queryset = TipoPlan.objects.all()
    serializer_class = TipoPlanSerializer

class TipoPlanUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = TipoPlan.objects.all()
    serializer_class = TipoPlanSerializer

class PlanListView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PeliculasListView(ListAPIView):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

class PeliculasUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = Peliculas.objects.all()
    serializer_class = PeliculasSerializer

class PersonaListView(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class LogListView(ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class RatingPeliculasListView(ListAPIView):
    queryset = RatingPeliculas.objects.all()
    serializer_class = RatingSerializer

class RatingPeliculasUpDeRe(RetrieveUpdateDestroyAPIView):
    queryset = RatingPeliculas.objects.all()
    serializer_class = RatingSerializer



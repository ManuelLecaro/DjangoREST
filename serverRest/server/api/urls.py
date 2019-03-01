from django.urls import path
from .views import TipoPlanViewSet, PlanViewSet, PeliculasViewSet, PersonaViewSet, LogViewSet
from .views import RatingPeliculasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tipoplan',TipoPlanViewSet,base_name='tipoplan')
router.register(r'plan', PlanViewSet, base_name="plan")
router.register(r'pelicula', PeliculasViewSet, base_name="pelicula")
router.register(r'persona', PersonaViewSet, base_name="persona")
router.register(r'log',LogViewSet, base_name="log")
router.register(r'rating',RatingPeliculasViewSet,base_name="ratings")
urlpatterns = router.urls
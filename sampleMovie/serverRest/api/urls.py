from django.urls import path
from .views import TipoPlanListView, PlanListView, PeliculasListView, PersonaListView, LogListView
from .views import RatingPeliculasListView, TipoPlanUpDeRe, PlanUpDeRe, PeliculasUpDeRe, PersonaUpDeRe,LogUpDeRe, RatingPeliculasUpDeRe

urlpatterns = [
    path('tipoplan/',TipoPlanListView.as_view()),
    path('tipoplan/<pk>',TipoPlanUpDeRe.as_view()),
    path('plan/', PlanListView.as_view()),
    path('plan/<pk>', PlanUpDeRe.as_view()),
    path('peli/', PeliculasListView.as_view()),
    path('peli/<pk>',PeliculasUpDeRe.as_view()),
    path('persona/',PersonaListView.as_view()),
    path('persona/<pk>',PersonaUpDeRe.as_view()),
    path('log/', LogListView.as_view()),
    path('log/<pk>',LogUpDeRe.as_view()),
    path('rating/',RatingPeliculasListView.as_view()),
    path('rating/<pk>',RatingPeliculasUpDeRe.as_view())
]
from django.contrib import admin

# Register your models here.
from .models import TipoPlan, Plan,Persona, Peliculas,Log,RatingPeliculas
admin.site.register(TipoPlan)
admin.site.register(Plan)
admin.site.register(Persona)
admin.site.register(Peliculas)
admin.site.register(Log)
admin.site.register(RatingPeliculas)
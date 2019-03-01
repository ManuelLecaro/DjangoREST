from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView
from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from movies.models import Log,RatingPeliculas,Persona,Plan,Peliculas
from movies.api.serializers import RatingSerializer, PeliculasSerializer, PersonaSerializer
from movies.forms import RatingForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model
User = get_user_model()

#from .controller import Controller

# Create your views here.

#Views make by functions without connection to the REST API
def MovieSearch(request):
	movie = Log.top_n_peliculas(10)
	contexto = {'pelicula':movie}
	return render(request,"index.html",contexto)

def ListaRating(request):
	peliculas=RatingPeliculas.allpeliculas()
	contexto={'peliculas':peliculas}
	return render(request,'list_rating.html',contexto)

def UserInfo(request):
    ids = request.user.id
    user = User.objects.get(id=ids)
    movies = RatingPeliculas.peliculasCal(ids)
    contexto = {'user':user,
                'peliculas':movies}
    return render(request,"list_user.html",contexto)

def PeliInfo(request):
    id = request.GET.get('peliId', "")
    movie = Peliculas.objects.get(id=id)
    promedio = RatingPeliculas.peliculasList(id)
    contexto = {'peliculas':movie,
                'promedio':promedio}
    print(promedio)
    return render(request,"list_pelicula.html",contexto)



'''def getSoapRequest(request):
    controller = Controller()
    plan = controller.listar()
    contexto = {'plan':plan}
    return render(request,"planlistar.html",contexto)  '''  






















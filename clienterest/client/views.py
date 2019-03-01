from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView
from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from client.models import Log,RatingPeliculas
from client.serializers import RatingSerializer, PeliculasSerializer, PersonaSerializer
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import requests
import json

#functions to connect to the API
@api_view(['GET', 'POST'])
def rating_list(request):
    """
	 enlista los trabajos , o crea un nuevo trabajo
 	"""
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        ratings = RatingPeliculas.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(ratings, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = RatingSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/trabajos/?page=' + str(nextPage),
         'prevlink': '/api/trabajos/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class RatingList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list_rating.html'

    def get(self, request):
        r = requests.get('')
        queryset = RatingPeliculas.allpeliculas()
        return Response({'peliculas': queryset})

class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rating_form.html'

    def get(self, request, pk):
        profile = get_object_or_404(RatingPeliculas, pk=pk)
        serializer = RatingSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(RatingPeliculas, pk=pk)
        print(profile)
        serializer = RatingSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('rating_listar')

class RatingDelete(DeleteView):
    model=RatingPeliculas
    template_name='rating_delete.html'
    success_url=reverse_lazy('rating_listar')
    
    def get_object(self, pk):
        profile = get_object_or_404(RatingPeliculas, pk=pk)
        return profile

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = RatingSerializer(event)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        rating = get_object_or_404(RatingPeliculas, pk=pk)
        if request.method == 'POST':
            rating.delete()
            return redirect('rating_listar')
        return render(request,'rating_delete.html',{'rating':rating})
#---------------------------------------------------------------------------------------------------------------
@api_view(['GET', 'POST', ])
def getRating(request):
    response = requests.get('http://127.0.0.1:7880/api/rating/')
    queryset = response.json()
    return render(request, 'list_rating.html',context={'peliculas': queryset})

@api_view(['GET', 'POST', ])
def updateRating(request,pk):
    if request.method == "GET":
        serializer = RatingSerializer(profile)
        return render(request,"rating_form.html",{'serializer': serializer})
    
    if request.method == 'POST':
        payload = request.data
        response = requests.post('http://127.0.0.1:7880/api/rating/'+pk,payload)
        return redirect('rating_listar')
    return render(request,"rating_form.html",{'serializer': serializer})

@api_view(['POST','GET', ])
def deleteRating(request, pk):
    valor = requests.get('http://127.0.0.1:7880/api/rating/'+pk)
    if request.method == 'POST':
        valor = requests.delete('http://127.0.0.1:7880/api/rating/'+pk)
        return redirect('rating_listar')
    return render(request,'rating_delete.html',{'rating':valor})

@api_view(['POST','GET',])
def createRating(request):
    #response = requests.get('http://127.0.0.1:7880/api/rating/')
    movies = requests.get('http://127.0.0.1:7880/api/pelicula/')
    people = requests.get('http://127.0.0.1:7880/api/persona/')
    people = people.json()
    movies = movies.json()
    #response = response.json()
    responseTotal = {
        "pelicula":movies,
        "persona":people,
    }
    if request.method == 'POST':
        movie = request.POST.get('movie',"")
        autor = request.POST.get('autor',"")
        calific = request.POST.get('cali',"")
        payload = {
            "pelicula": movie,
            "persona": autor,
            "cali": calific
        }
        print(payload)
        valor = requests.post('http://127.0.0.1:7880/api/rating/',data=payload)
        return redirect('rating_listar')
    return render(request, 'list_crear.html',{'rating':responseTotal})


@api_view(['POST','GET',])
def updateRating(request, pk):
    valor = requests.get('http://127.0.0.1:7880/api/rating/'+pk)
    movies = requests.get('http://127.0.0.1:7880/api/pelicula/')
    people = requests.get('http://127.0.0.1:7880/api/persona/')
    valor = valor.json()
    people = people.json()
    movies = movies.json()
    responseTotal = {
        "valor": valor,
        "pelicula":movies,
        "persona":people,
    }
    if request.method == 'POST':
        movie = request.POST.get('movie',"")
        autor = request.POST.get('autor',"")
        calific = request.POST.get('cali',"")
        payload = {
            "pelicula": movie,
            "persona": autor,
            "cali": calific
        }
        print(payload)
        valor = requests.put('http://127.0.0.1:7880/api/rating/'+pk+"/",data=(payload))
        return redirect('rating_listar')
    return render(request,'rating_form.html',{'rating':responseTotal})











from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libro, Receta
from .serializer import Libro_Serializer, receta_Serializer, recetaLista_Serializer,LibroLista_Serializer
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q

@api_view(['GET'])
def libroLista(request):
    libros = Libro.objects.all()
    serializer = LibroLista_Serializer(libros, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_audiolibro(request, id_libro):
    try:
        # Buscamos el audiolibro por su ID
        audiolibro = Libro.objects.get(id_libro=id_libro)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializamos el audiolibro y lo devolvemos en la respuesta
    serializer = Libro_Serializer(audiolibro)
    return Response(serializer.data)

@api_view(['GET'])
def recetaLista(request):
    recetas = Receta.objects.all()  # Obtiene todas las recetas
    serializer = recetaLista_Serializer(recetas, many=True)
    return Response(serializer.data)
        
@api_view(['GET'])
def get_receta(request, id_receta):
    try:
        # Buscamos el audiolibro por su ID
        receta = Receta.objects.get(id_receta=id_receta)
    except Receta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializar la receta, incluyendo los pasos
    serializer = receta_Serializer(receta)
    return Response(serializer.data)

@api_view(['GET'])
def buscar_audiolibros(request):
    query = request.GET.get('search', '')  # Obtiene el término de búsqueda de la URL
    if query:
        audiolibros = Libro.objects.filter(nombre_libro__icontains=query)  # Filtra por coincidencia parcial
    else:
        audiolibros = Libro.objects.all()  # Devuelve todos los audiolibros si no hay búsqueda

    serializer = Libro_Serializer(audiolibros, many=True)  # Serializa los datos
    return Response(serializer.data, status=status.HTTP_200_OK)
from django.urls import path
from .views import libroLista, get_audiolibro, recetaLista, get_receta, buscar_audiolibros

urlpatterns = [
    path('libros/', libroLista, name='libro-lista'),
    path('libros/<int:id_libro>/', get_audiolibro, name='get-audiolibro'),
    path('recetas/', recetaLista, name='receta-lista'),
    path('recetas/<int:id_receta>/', get_receta, name='get-receta'),
    path('libros/buscar/', buscar_audiolibros, name='buscar_audiolibros'),
]
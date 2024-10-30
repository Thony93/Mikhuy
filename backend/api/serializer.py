from rest_framework import serializers
from .models import Libro, Receta, Paso, Ingrediente, RecetaHasIngrediente, TipoUnidad, Autor, AutorHasLibro

#Este serializador es para convertir datos de la BD en formato JSON.

#Aqui van puro serializadores de tablas que no se comunican con otras.
class Paso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Paso
        fields = '__all__'
class Ingrediente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre_ingrediente', 'url_foto_ingrediente']
class TipoUnidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = ['nombre_unidad']
class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

#Aqui van serializadores que se comunican con otros, pero son intermediarios.
class RecetaHasIngrediente_Serializer(serializers.ModelSerializer):
    ingrediente = Ingrediente_Serializer(source='id_ingrediente_ingrediente', read_only=True)
    unidad = TipoUnidad_Serializer(source='id_unidad_tipo_unidad', read_only=True)
    class Meta:
        model = RecetaHasIngrediente
        fields = ['cantidad', 'ingrediente', 'unidad']
class AutorHasLibro_Serializer(serializers.ModelSerializer):
    autor = Autor_Serializer(source='id_autor_autor', read_only=True)
    class Meta:
        model = AutorHasLibro
        fields = '__all__'

#Aqui van serializadore que (yo les diré) son los principales.
class receta_Serializer(serializers.ModelSerializer):
    pasos = Paso_Serializer(many=True, read_only=True)  # Relación entre Receta y Paso
    ingredientes = RecetaHasIngrediente_Serializer(source='recetahasingrediente_set', many=True, read_only=True)
    class Meta:
        model = Receta
        fields = '__all__'
class Libro_Serializer(serializers.ModelSerializer):
    autores = AutorHasLibro_Serializer(source='AutorHasLibro_set', many=True, read_only=True)
    class Meta:
        model = Libro
        fields = '__all__'

#Estos últimos son los mismos que los 2 de arriba, sólo que con estos no tardará en cargar más
class recetaLista_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['id_receta', 'nombre_receta', 'url_imagen']
class LibroLista_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id_libro', 'nombre_libro', 'url_imagen_portada', 'fecha_publicacion']
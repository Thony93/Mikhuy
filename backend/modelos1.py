# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clasificador(models.Model):
    id_clasificador = models.AutoField(primary_key=True)
    nombre_clasificador = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'CLASIFICADOR'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    url_libro = models.CharField(blank=True, null=True)
    url_audio = models.CharField(blank=True, null=True)
    nombre_libro = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    url_imagen_portada = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LIBRO'


class LibroTieneTipos(models.Model):
    id_tipo_tipo_clasificador = models.OneToOneField('TipoClasificador', models.DO_NOTHING, db_column='id_tipo_TIPO_CLASIFICADOR', primary_key=True)  # Field name made lowercase. The composite primary key (id_tipo_TIPO_CLASIFICADOR, id_libro_LIBRO) found, that is not supported. The first column is selected.
    id_libro_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro_LIBRO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIBRO_TIENE_TIPOS'
        unique_together = (('id_tipo_tipo_clasificador', 'id_libro_libro'),)


class Paso(models.Model):
    num_paso = models.SmallAutoField(primary_key=True)  # The composite primary key (num_paso, id_receta_RECETA) found, that is not supported. The first column is selected.
    nombre_paso = models.CharField(blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)
    imagen = models.CharField(blank=True, null=True)
    id_receta_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='id_receta_RECETA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PASO'
        unique_together = (('num_paso', 'id_receta_receta'),)


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_receta = models.CharField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)
    porcion = models.SmallIntegerField(blank=True, null=True)
    tiempo = models.TimeField(blank=True, null=True)
    dificultad = models.SmallIntegerField(blank=True, null=True)
    url_imagen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RECETA'


class TipoClasificador(models.Model):
    id_tipo = models.SmallAutoField(primary_key=True)
    id_clasificador_clasificador = models.ForeignKey(Clasificador, models.DO_NOTHING, db_column='id_clasificador_CLASIFICADOR', blank=True, null=True)  # Field name made lowercase.
    nombre_tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_CLASIFICADOR'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre_ingrediente = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingrediente'

from django.db import models


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AUTOR'


class AutorHasLibro(models.Model):
    id_autor_autor = models.OneToOneField(Autor, models.DO_NOTHING, db_column='id_autor_AUTOR', primary_key=True)  # Field name made lowercase. The composite primary key (id_autor_AUTOR, id_libro_LIBRO) found, that is not supported. The first column is selected.
    id_libro_libro = models.ForeignKey('Libro', models.DO_NOTHING, db_column='id_libro_LIBRO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTOR_has_LIBRO'
        unique_together = (('id_autor_autor', 'id_libro_libro'),)


class Clasificador(models.Model):
    id_clasificador = models.AutoField(primary_key=True)
    nombre_clasificador = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'CLASIFICADOR'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(db_column='Id_ingrediente', primary_key=True)  # Field name made lowercase.
    nombre_ingrediente = models.CharField(max_length=200, blank=True, null=True)
    url_foto_ingrediente = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INGREDIENTE'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    url_libro = models.CharField(blank=True, null=True)
    url_audio = models.CharField(blank=True, null=True)
    nombre_libro = models.CharField(max_length=100, blank=True, null=True)
    url_imagen_portada = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)
    fecha_publicacion = models.CharField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LIBRO'


class LibroHasReceta(models.Model):
    id_receta_receta = models.OneToOneField('Receta', models.DO_NOTHING, db_column='id_receta_RECETA', primary_key=True)  # Field name made lowercase. The composite primary key (id_receta_RECETA, id_libro_LIBRO) found, that is not supported. The first column is selected.
    id_libro_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro_LIBRO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIBRO_has_RECETA'
        unique_together = (('id_receta_receta', 'id_libro_libro'),)


class LibroHasSubclasificador(models.Model):
    id_subclasificador_subclasificador = models.OneToOneField('Subclasificador', models.DO_NOTHING, db_column='id_subclasificador_SUBCLASIFICADOR', primary_key=True)  # Field name made lowercase. The composite primary key (id_subclasificador_SUBCLASIFICADOR, id_libro_LIBRO) found, that is not supported. The first column is selected.
    id_libro_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro_LIBRO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIBRO_has_SUBCLASIFICADOR'
        unique_together = (('id_subclasificador_subclasificador', 'id_libro_libro'),)


class Paso(models.Model):
    num_paso = models.SmallAutoField(primary_key=True)  # The composite primary key (num_paso, id_receta_RECETA) found, that is not supported. The first column is selected.
    nombre_paso = models.CharField(blank=True, null=True)
    descripcion = models.CharField(blank=True, null=True)
    url_imagen = models.CharField(blank=True, null=True)
    id_receta_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='id_receta_RECETA', related_name='pasos')  # Field name made lowercase.

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
    id_tipo_receta_tipo_receta = models.ForeignKey('TipoReceta', models.DO_NOTHING, db_column='id_tipo_receta_TIPO_RECETA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECETA'


class RecetaHasIngrediente(models.Model):
    id_ingrediente_ingrediente = models.OneToOneField(Ingrediente, models.DO_NOTHING, db_column='Id_ingrediente_INGREDIENTE', primary_key=True)  # Field name made lowercase. The composite primary key (Id_ingrediente_INGREDIENTE, id_receta_RECETA) found, that is not supported. The first column is selected.
    id_receta_receta = models.ForeignKey(Receta, models.DO_NOTHING, db_column='id_receta_RECETA')  # Field name made lowercase.
    id_unidad_tipo_unidad = models.ForeignKey('TipoUnidad', models.DO_NOTHING, db_column='ID_UNIDAD_TIPO_UNIDAD')  # Field name made lowercase.
    cantidad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RECETA_HAS_INGREDIENTE'
        unique_together = (('id_ingrediente_ingrediente', 'id_receta_receta'),)


class Subclasificador(models.Model):
    id_subclasificador = models.AutoField(primary_key=True)
    id_clasificador_clasificador = models.ForeignKey(Clasificador, models.DO_NOTHING, db_column='id_clasificador_CLASIFICADOR', blank=True, null=True)  # Field name made lowercase.
    nombre_subclasificador = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SUBCLASIFICADOR'


class TipoReceta(models.Model):
    id_tipo_receta = models.SmallAutoField(primary_key=True)
    nombre_tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_RECETA'


class TipoUnidad(models.Model):
    id_unidad = models.SmallAutoField(db_column='ID_UNIDAD', primary_key=True)  # Field name made lowercase.
    nombre_unidad = models.CharField(db_column='NOMBRE_UNIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_UNIDAD'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

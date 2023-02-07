# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
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


class Game(models.Model):
    id_game = models.AutoField(primary_key=True)
    developer = models.CharField(max_length=40, blank=True, null=True)
    year_release = models.DateField(blank=True, null=True)
    tittle = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    punctuation = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    descriptionn = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class GameGender(models.Model):
    id_game_gender = models.AutoField(primary_key=True)
    id_game = models.ForeignKey(Game, models.DO_NOTHING, db_column='id_game')
    id_gender = models.ForeignKey('Gender', models.DO_NOTHING, db_column='id_gender')

    class Meta:
        managed = False
        db_table = 'game_gender'


class GameUser(models.Model):
    id_game_user = models.AutoField(primary_key=True)
    id_game = models.ForeignKey(Game, models.DO_NOTHING, db_column='id_game')
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    game_state = models.CharField(max_length=30, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    times_pass = models.IntegerField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_user'


class Gender(models.Model):
    id_gender = models.AutoField(primary_key=True)
    namee = models.CharField(max_length=80, blank=True, null=True)
    tittle = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender'


class Movie(models.Model):
    id_movie = models.AutoField(primary_key=True)
    director = models.CharField(max_length=40, blank=True, null=True)
    year_release = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    guion = models.CharField(max_length=50, blank=True, null=True)
    tittle = models.CharField(max_length=50, blank=True, null=True)
    cast = models.CharField(max_length=500, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    punctuation = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    descriptionn = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieGender(models.Model):
    id_movie_gender = models.AutoField(primary_key=True)
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='id_movie')
    id_gender = models.ForeignKey(Gender, models.DO_NOTHING, db_column='id_gender')

    class Meta:
        managed = False
        db_table = 'movie_gender'


class MovieUser(models.Model):
    id_movie_user = models.AutoField(primary_key=True)
    id_movie = models.IntegerField(blank=True, null=True)
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    movie_state = models.CharField(max_length=30, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    times_view = models.IntegerField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_user'


class Serie(models.Model):
    id_serie = models.AutoField(primary_key=True)
    director = models.CharField(max_length=40, blank=True, null=True)
    year_release = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=50, blank=True, null=True)
    tittle = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    punctuation = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    descriptionn = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie'


class SerieGender(models.Model):
    id_serie_gender = models.AutoField(primary_key=True)
    id_serie = models.ForeignKey(Serie, models.DO_NOTHING, db_column='id_serie')
    id_gender = models.ForeignKey(Gender, models.DO_NOTHING, db_column='id_gender')

    class Meta:
        managed = False
        db_table = 'serie_gender'


class SerieUser(models.Model):
    id_serie_user = models.AutoField(primary_key=True)
    id_serie = models.ForeignKey(Serie, models.DO_NOTHING, db_column='id_serie')
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    serie_state = models.CharField(max_length=30, blank=True, null=True)
    director = models.CharField(max_length=40, blank=True, null=True)
    year_release = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=50, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    tittle = models.CharField(max_length=50, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_user'


class Userr(models.Model):
    id_user = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    session_token = models.CharField(max_length=1000, blank=True, null=True)
    descriptionn = models.CharField(max_length=1000, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    banner = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userr'

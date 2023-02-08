# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GameUser(models.Model):
    id_game_user = models.AutoField(primary_key=True)
    id_game = models.IntegerField()
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    game_state = models.CharField(max_length=30, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    times_pass = models.IntegerField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_user'


class MovieUser(models.Model):
    id_movie_user = models.AutoField(primary_key=True)
    id_movie = models.IntegerField()
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    movie_state = models.CharField(max_length=30, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    times_view = models.IntegerField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_user'


class SerieUser(models.Model):
    id_serie_user = models.AutoField(primary_key=True)
    id_serie = models.IntegerField()
    id_user = models.ForeignKey('Userr', models.DO_NOTHING, db_column='id_user')
    serie_state = models.CharField(max_length=30, blank=True, null=True)
    notes = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    times_view = models.IntegerField(blank=True, null=True)
    final_date = models.DateTimeField(blank=True, null=True)
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

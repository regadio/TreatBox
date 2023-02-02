import json
import jwt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *
from django.forms.models import model_to_dict

# Create your views here.

#Crear vista de /login
@csrf_exempt
def start_session_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        try:
            user = Userr.objects.get(nickname=username, pass_field=password)
            user.session_token = generate_token(user)
            user.save()
            return JsonResponse({'session_token': user.session_token}, status=200)
        except Userr.DoesNotExist:
            return JsonResponse({'error': 'La contraseña o el usuario no existen'}, status=400)
    return HttpResponse(status=405)

def generate_token(user):
    payload = {
        'user_id': user.id_user,
        'username': user.nickname
    }
    secret = 'azulafull'
    token = jwt.encode(payload, secret, algorithm='HS256').decode('utf-8')
    return token


#Crear vista de /register
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_confirm = data.get('passwordConfirm')

        # Validar que todos los campos esten completos
        if not all([username, email, password, password_confirm]):
            return JsonResponse({'error': 'Faltan parámetros'}, status=400)

        # Validar que las contraseñas coincidan
        if password != password_confirm:
            return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

        # Validar que el usuario no exista
        if Userr.objects.filter(nickname=username).exists():
            return JsonResponse({'error': 'El usuario ya existe'}, status=409)

        # Crear el usuario
        user = Userr(nickname=username, email=email, pass_field=password)
        user.save()

        # Crear y devolver el token de sesion
        # session_token = create_session_token(user)
        # user.session_token = session_token
        # user.save()
        # return JsonResponse({'sessionToken': session_token}, status=201)
        return JsonResponse({'OK': 'El usuario registrado'}, status=200)

    return HttpResponse(status=405)



#Crear vista de /user
@csrf_exempt
def user(request, username):
    if request.method == 'GET':
        try:
            user = Userr.objects.get(nickname=username)
            return JsonResponse(model_to_dict(user))
        except Userr.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)

#Crear vista de GET /films{id}
@csrf_exempt
def film_saved_view(request, id_solicitado):
    if request.method == 'GET':
        try:
            pelicula = MovieUser.objects.get(id = id_solicitado)
            return JsonResponse(model_to_dict(pelicula))
        except MovieUser.DoesNotExist:
            return HttpResponse(status=404) #si no encuentra la película
    else:
        return HttpResponse(status=405) #si no funciona la petición get



#Crear vista de GET /series{id}
@csrf_exempt
def series_saved_view(request, id_solicitado):
    if request.method == 'GET':
        try:
            serie = SerieUser.objects.get(id = id_solicitado)
            return JsonResponse(model_to_dict(serie))
        except SerieUser.DoesNotExist:
            return HttpResponse(status=404) #si no encuentra la serie
    else:
        return HttpResponse(status=405) #si no funciona la petición get


#Crear vista de GET /videojuegos{id}
@csrf_exempt
def games_saved_view(request, id_solicitado):
    if request.method == 'GET':
        try:
            game = GameUser.objects.get(id = id_solicitado)
            return JsonResponse(model_to_dict(game))
        except GameUser.DoesNotExist:
            return HttpResponse(status=404) 
    else:
        return HttpResponse(status=405) #si no funciona la petición get


#Crear vista de Put /films/{id}/favorites
def movie_insert_view(request, id_peliculas, id_usuario):
    if request.method == 'PUT':
        data = json.loads(request.body)
        movie_state = data.get('movie_state')
        notes = data.get('notes')
        times_view = data.get('times_view')
        final_date = data.get('final_date')
        comment = data.get('comment')
        try:
            movie = MovieUser.objects.get(id = id_peliculas,id_user=id_usuario, movie_state=movie_state,notes=notes, times_view=times_view, final_date=final_date, comment=comment)
            movie.save()
        except MovieUser.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405) #si no funciona la petición
    
#Crear vista de Put /series/{id}/favorites
def series_insert_view(request, id_series, id_usuario):
    if request.method == 'PUT':
        data = json.loads(request.body)
        serie_state = data.get('serie_state')
        year_release = data.get('year_release')
        notes = data.get('notes')
        comment = data.get('comment')
        try:
            serie = SerieUser.objects.get(id = id_series,id_user=id_usuario,serie_state=serie_state, year_release=year_release, notes=notes,comment=comment)
            serie.save()
        except SerieUser.DoesNotExist:
            return HttpResponse(status=404) 
    else:
        return HttpResponse(status=405) #si no funciona la petición


#Crear vista de Put /games/{id}/favorites
def games_insert_view(request, id_juegos, id_usuario):
    if request.method == 'PUT':
        data = json.loads(request.body)
        game_state = data.get('game_state')
        notes = data.get('notes')
        times_pass = data.get('times_pass')
        final_date = data.get('final_date')
        comment = data.get('comment')
        try:
            game = GameUser.objects.get(id = id_juegos,id_user=id_usuario,game_state=game_state,times_pass=times_pass,final_date=final_date, notes=notes,comment=comment)
            game.save()
        except GameUser.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405) #si no funciona la petición


#Crear una vista de GET /users/{nick}



#Crear una vista de un PUT /profile para cambiar nick y/o descripción y/o imgPerfil y/o banner



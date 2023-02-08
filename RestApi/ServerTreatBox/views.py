import json
import jwt
import logging
from django.db.models import Avg
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
    secret = 'secreto'
    token = jwt.encode(payload, secret, algorithm='HS256')
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
def user_data(request, username):
    if request.method == 'GET':
        try:
            user = Userr.objects.filter(nickname=username).values()
            return JsonResponse(list(user), safe=False)
        except Userr.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def user_editdata(request, username):
    if request.method == 'PUT':
        data = json.loads(request.body)
        descriptionn = data.get('descriptionn')
        try:
            user = Userr.objects.get(nickname=username)
            user.nickname = username
            user.descriptionn = descriptionn
            user.save()
            return HttpResponse(status=200)
        except Userr.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)
    


#Crear vista de GET de peliculas totales de un usuario
@csrf_exempt
def total_saved_view(request, username):
    if request.method == 'GET':
        try:
            user = Userr.objects.get(nickname=username)
            total_pelis = MovieUser.objects.filter(id_user=user.id_user).count()
            total_series = SerieUser.objects.filter(id_user=user.id_user).count()
            avg_pelis = MovieUser.objects.filter(id_user=user.id_user).aggregate(Avg('notes'))
            avg_series = SerieUser.objects.filter(id_user=user.id_user).aggregate(Avg('notes'))

            return JsonResponse({'total_pelis': total_pelis,'total_series': total_series,'avg_pelis': avg_pelis['notes__avg'],'avg_series': avg_series['notes__avg']})
        except Userr.DoesNotExist:
            return HttpResponse(status=404) #si no encuentra el usuario
        except MovieUser.DoesNotExist:
            return HttpResponse(status=404) # si no se encuentra la película asociada al usuario
        except SerieUser.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405) #si no funciona la petición get




logging.basicConfig(level=logging.DEBUG)

#Crear vista de Put /films/favorites
@csrf_exempt
def movie_insert_view(request,id_pelicula):
    logging.debug("Este es un mensaje de depuración")
    if request.method == 'PUT':
        data = json.loads(request.body)
        movie_state = data.get('movie_state')
        notes = data.get('notes')
        times_view = data.get('times_view')
        final_date = data.get('final_date')
        comment = data.get('comment')
        username = data.get('username')
        try:
            user = Userr.objects.get(nickname=username)
            movie, created = MovieUser.objects.get_or_create(id_movie=id_pelicula, id_user=user)
            movie.movie_state = movie_state
            movie.notes = notes
            movie.times_view = times_view
            movie.final_date = final_date
            movie.comment = comment
            movie.save()
            return HttpResponse(status=200)
        except MovieUser.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405) #si no funciona la petición
    
#Crear vista de Put /series/{id}/favorites
@csrf_exempt
def series_insert_view(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        id_series =data.get('id_serie')
        id_usuario =data.get('id_user')
        serie_state = data.get('serie_state')
        year_release = data.get('year_release')
        notes = data.get('notes')
        comment = data.get('comment')
        try:
            serie = SerieUser(id_series = id_series,id_user=id_usuario,serie_state=serie_state, year_release=year_release, notes=notes,comment=comment)
            serie.save()
        except SerieUser.DoesNotExist:
            return HttpResponse(status=404) 
    else:
        return HttpResponse(status=405) #si no funciona la petición




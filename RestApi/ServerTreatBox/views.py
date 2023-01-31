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
            user.session_token = generate_token()
            user.save()
            return JsonResponse({'session_token': user.session_token}, status=200)
        except Userr.DoesNotExist:
            return JsonResponse({'error': 'La contraseña o el usuario no existen'}, status=400)
    return HttpResponse(status=405)

def generate_token():
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
        except Userr.DoesNotExist:
            return HttpResponse(status=404) #si no encuentra la película
    else:
        return HttpResponse(status=405) #si no funciona la petición get



#Crear vista de GET /series{id}

#Crear vista de GET /videojuegos{id}



#Crear vista de Put /films/{id}/favorites
    
#Crear vista de Put /games/{id}/favorites



#Crear vista de Put /series/{id}/favorites



#Crear una vista de GET /users/{nick}



#Crear una vista de un PUT /profile para cambiar nick y/o descripción y/o imgPerfil y/o banner



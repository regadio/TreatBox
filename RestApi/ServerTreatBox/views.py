import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

#Crear vista de /sessions
def start_session_view (request):
    if request.method == 'POST':
        data = json.loads(request.data)
        username = data.get('username')
        password = data.get('password')

        if Userr.objects.filter(nickname=username).exists() | Userr.objects.filter(pass_field=password).exists():
            user=Userr(session_token=generate_token(session_token))
        else:
            return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)
   
    return HttpResponse(status=405)
def generate_token (generate_token):
    return "ASDFASDFASDFLASKDF"


#Crear vista de /register
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.data)
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



#Crear vista de /films
def film_detail_view(request, id_solicitado):
    if request.method == 'GET':
        pelicula = MovieUser.objects.get(id = id_solicitado)
        resultado = {
            'id_movie': MovieUser.id_movie,
            'movie_state': MovieUser.movie_state,
            'times_view': MovieUser.times_view,
            'notes': MovieUser.notes,
            'final_date': MovieUser.final_date,
            'comment': MovieUser.comment   
        }
        return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})
    


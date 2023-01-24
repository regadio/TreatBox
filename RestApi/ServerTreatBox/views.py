import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

#Crear vista de /sessions
def sessions_view(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')

        auth_result = authenticate_user(username, password)
        if auth_result:
            session_token = generate_session_token()
            return JsonResponse({'sessionToken': session_token}, status=201)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=400)

def authenticate_user(username, password):
    if username == "Paco" and password == "Abc123":
        return True
    return False

def generate_session_token():
    return "ASDFASDFASDFLASKDF"


#Crear vista de /users
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nickname = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_confirm = data.get('passwordConfirm')

        # Validar que todos los campos esten completos
        if not all([nickname, email, password, password_confirm]):
            return JsonResponse({'error': 'Faltan parámetros'}, status=400)

        # Validar que las contraseñas coincidan
        if password != password_confirm:
            return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

        # Validar que el usuario no exista
        if Userr.objects.filter(nickname=nickname).exists():
            return JsonResponse({'error': 'El usuario ya existe'}, status=409)

        # Crear el usuario
        user = Userr(nickname=nickname, email=email, pass_field=password)
        user.save()

        # Crear y devolver el token de sesion
        # session_token = create_session_token(user)
        # user.session_token = session_token
        # user.save()
        # return JsonResponse({'sessionToken': session_token}, status=201)
        return JsonResponse({'OK': 'El usuario registrado'}, status=200)

    return HttpResponse(status=405)

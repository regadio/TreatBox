import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MovieUser
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
    


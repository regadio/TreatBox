import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
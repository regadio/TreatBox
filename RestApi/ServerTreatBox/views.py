from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ejemplo_view(request):
    return HttpResponse("Este es un ejemplo de endpoint en Django.")
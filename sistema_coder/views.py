from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario/a"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


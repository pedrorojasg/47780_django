from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario/a"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario/a, fecha: {hoy.day}/{hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http


def saludar_con_html(request):
    contexto = {
        "profesor": "Pedro",
        "tutores": ["Mariano", "Ruben", "Luciano"],
        "comision": 47780,
    }
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

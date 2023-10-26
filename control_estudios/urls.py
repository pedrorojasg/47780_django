from django.urls import path

from control_estudios.views import listar_estudiantes

# Son las URLS de la app control_estudios
urlpatterns = [
    path("estudiantes/", listar_estudiantes),
]

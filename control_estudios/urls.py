from django.urls import path

from control_estudios.views import listar_estudiantes, listar_cursos, crear_curso

# Son las URLS de la app control_estudios
urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
]

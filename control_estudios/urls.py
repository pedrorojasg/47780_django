from django.urls import path

from control_estudios.views import (
    listar_estudiantes, listar_cursos, crear_curso, buscar_cursos,
    eliminar_curso, editar_curso, EstudianteListView
)

# Son las URLS de la app control_estudios
urlpatterns = [
    # URLS de cursos (clases)
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de estudiantes (clases)
    path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
]

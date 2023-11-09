from django.contrib import admin
from django.urls import path

from perfiles.views import registro


urlpatterns = [
    # URLS Usuario y sesion
    path('registro/', registro, name="registro"),
]
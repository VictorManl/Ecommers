from django.urls import path

from core.views import Inicio, Crearproducto

urlpatterns = [
    path('Inicio', Inicio.as_view(), name="Inicio"),
    path('Inicio/crear_producto/', Crearproducto.as_view(), name ='Crear_producto'),
]

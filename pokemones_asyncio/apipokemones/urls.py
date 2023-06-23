from django.urls import path

from .views.asyncio import pokemon_list_async
from .views.original import pokemon_list

urlpatterns = [
    #   inicio
    path('', pokemon_list, name="index"),

    #   listar
    path('lista-original/', pokemon_list, name="pokemon_lista_original"),
    path('lista-async/', pokemon_list_async, name="pokemon_lista_async"),
]

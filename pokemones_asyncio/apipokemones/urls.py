from django.urls import path

from .views.original import pokemon_list

urlpatterns = [
    #   inicio
    path('', pokemon_list, name="index"),

    #   listar
    path('lista-original/', pokemon_list, name="pokemon_lista_original"),
]

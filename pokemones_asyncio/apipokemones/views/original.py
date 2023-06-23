import time

from django.shortcuts import render, reverse

from apipokemones.api.api_original import get_pokemons, get_imagen


def pokemon_list(request):
    inicio_tiempo = time.time()
    pokemones = get_pokemons()
    pokemones_con_imagen = []
    for pokemon in pokemones:
        pokemones_con_imagen.append(get_imagen(pokemon['url']))
    cantidad = len(pokemones_con_imagen)
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_list.html', {
        'pokemones': pokemones_con_imagen,
        'tiempo_carga': tiempo_carga,
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES ORIGINAL'
    })
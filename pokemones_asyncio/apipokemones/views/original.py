import time

from django.shortcuts import render, reverse

from apipokemones.api.api_original import get_pokemons, get_imagen


def pokemon_list(request):
    inicio_tiempo = time.time()
    contexto = get_pokemons()
    id = 0
    contexto2 = {}
    for pokemon in contexto:
        id += 1
        imagen = get_imagen(pokemon['url'])
        contexto2[id] = {
            'id': imagen.get('id'),
            'nombre': pokemon['name'],
            'url': pokemon['url'],
            'imagen': imagen.get('imagen'),
        }
    cantidad = len(contexto2)
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_list.html', {
        'pokemones': contexto2,
        'tiempo_carga': tiempo_carga,
        'detail_url': 'pokemon_detallefuncion',
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES NORMAL'
    })
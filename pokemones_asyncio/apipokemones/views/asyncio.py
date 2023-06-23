import time

import asyncio
import aiohttp

from django.shortcuts import render

from apipokemones.api.api_asyncio import get_pokemones, get_imagen_pokemon


async def pokemon_list_async(request):
    task = []
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        """Se ejecuta la tarea de obtener la lista de pokemones"""
        pokemones = await get_pokemones(session)
        for pokemon in pokemones:
            task.append(get_imagen_pokemon(session, pokemon['url']))
        """ Se manda a esperar una promesa que ejecuta lo que se encuentra en la lista de tareas.
            El cual nos da como resultado una lista de diccionarios con  los datos de los pokemones
            (Id, nombre y url de su imagen)
        """
        pokemones_con_imagenes = await asyncio.gather(*task)
        cantidad = len(pokemones_con_imagenes)
        tiempo_carga = time.time() - inicio_tiempo
        tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
        return render(request, 'pokemones/pokemon_list.html', {
            'pokemones': pokemones_con_imagenes,
            'tiempo_carga': tiempo_carga,
            'cantidad': cantidad,
            'titulo': 'LISTA DE POKEMONES CON ASYNCIO'
        })
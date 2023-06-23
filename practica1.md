# Paso 1
## Hacer fork del proyecto y hacer git clone a su fork 
    https://github.com/miguelsantos-wh/pokemones-asyncio
# Paso 2
## En el entorno creado instalar dependencias
    pip install -r requirements.txt
# Paso 3
## Crear corrutina para obtener una lista de pokemones con asyncio (Es necesario el parametro “session”) Ejemplo:
    async def get_pokemones(session):
        url = <<endpoint>>
        async with session.get(url) as resp:
            response = await resp.json()
            results = response.get(<<list_result>>)
            return results
# Paso 4
## Crear una corrutina que obtenga la imagen y el nombre del pokemon en base al endpoint obtenido del pokemon (Es necesario el parametro “session” Ejemplo:
    async def get_imagen_pokemon(session, url):
        async with session.get(url) as resp:
            response_json = await resp.json()
            sprite = response_json['sprites']
            id = response_json['id']
            nombre = response_json['name']
            data = {
                'imagen': sprite['front_default'],
                'id': id,
                'nombre': nombre,
            }
            return data
# Paso 5
## Crear vista para poder listar los pokemones con sus imagenes usando Asyncio. Importante importar librerias asyncio y aiohttp Ejemplo:
    import asyncio
    import aiohttp
    async def pokemon_list(request):
        task = []
        async with aiohttp.ClientSession() as session:
            """Se ejecuta la tarea de obtener la lista de pokemones"""
            pokemones = await get_pokemons_async_aio(session)
            << Se recorre los pokemones para llenar la lista de tareas >>
            << Ejemplo llenado de la tarea >>
            task.append(get_imagen_async_aio(session, pokemon['url']))
            << Fin Ejemplo llenado de la tarea >>
            """ Se manda a esperar una promesa que ejecuta lo que se encuentra en la lista de tareas.
                El cual nos da como resultado una lista de diccionarios con  los datos de los pokemones
                (Id, nombre y url de su imagen)
            """
            pokemones_con_imagenes = await asyncio.gather(*task)
            return render(request, 'pokemones/pokemon_list.html', {
                'pokemones': pokemones_con_imagenes,
                'titulo': 'LISTA DE POKEMONES CON ASYNCIO'
            })
# Paso 6 
## Verificar que la lista de pokemones se vea
# Nota: Se puede jugar con el endpoint para ver el tiempo que se tarda cuando se aumenta el limite de pokemones a traer
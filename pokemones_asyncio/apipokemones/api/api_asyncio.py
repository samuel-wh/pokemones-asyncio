async def get_pokemones(session):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=100'
    async with session.get(url) as resp:
        response = await resp.json()
        results = response.get('results', [])
        return results


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

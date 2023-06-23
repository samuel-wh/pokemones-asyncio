import requests


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=100'
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload.get('results', [])
    return results


def get_imagen(url):
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data

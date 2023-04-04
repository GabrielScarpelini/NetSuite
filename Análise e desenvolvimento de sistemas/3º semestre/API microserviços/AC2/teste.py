import requests
from pprint import pprint


site_pokeapi = "https://pokeapi.co"

def nome_do_pokemon(numero):
    url = f'{site_pokeapi}/api/v2/pokemon/{numero}/'
    response = requests.get(url)
    data = response.json()
    pokemon = data['name']
    return pokemon

nome_do_pokemon(39)

# def numero_do_pokemon(nome):
#     url = f'{site_pokeapi}/api/v2/pokemon/{nome}'
#     response = requests.get(url)
#     data = response.json()
#     return data['id']

# print(numero_do_pokemon('mewtwo'))

# def color_of_pokemon(nome_num):
#     url = f'{site_pokeapi}/api/v2/pokemon-species/{nome_num}/'
#     response = requests.get(url)
#     data = response.json()
#     return data['color']['name']

# print(color_of_pokemon(1))

dic_cores = {
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}

# def cor_do_pokemon(nome):
#     url = f'{site_pokeapi}/api/v2/pokemon-species/{nome}/'
#     response = requests.get(url)
#     data = response.json()
#     return dic_cores[data['color']['name']]

# print(cor_do_pokemon('clefable'))

def tipos_do_pokemon(nome):
    url = f'{site_pokeapi}/api/v2/pokemon/{nome}/'
    response = requests.get(url)
    data = response.json()
    return data['types'][0]['type']['name']

print(tipos_do_pokemon('snorlax'))


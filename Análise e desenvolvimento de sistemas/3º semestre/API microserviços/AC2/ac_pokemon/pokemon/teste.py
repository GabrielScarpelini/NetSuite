import requests
from pprint import pprint


site_pokeapi = "https://pokeapi.co"

# def nome_do_pokemon(numero):
#     url = f'{site_pokeapi}/api/v2/pokemon/{numero}/'
#     response = requests.get(url)
#     data = response.json()
#     pokemon = data['name']
#     return pokemon

# nome_do_pokemon(39)

# def numero_do_pokemon(nome):
#     url = f'{site_pokeapi}/api/v2/pokemon/{nome}'
#     response = requests.get(url)
#     data = response.json()
#     return data['id']

# print(numero_do_pokemon('mewtwo'))

# def color_of_pokemon(nome_num):
#     url = f'{site_pokeapi}/api/v2/pokemon-species/{nome_num.lower()}/'
#     response = requests.get(url)
#     data = response.json()
#     return data['color']['name']

# print(color_of_pokemon('ditto'))

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
dic_tipos = {
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}


# def cor_do_pokemon(nome):
#     url = f'{site_pokeapi}/api/v2/pokemon-species/{nome}/'
#     response = requests.get(url)
#     data = response.json()
#     return dic_cores[data['color']['name']]

# print(cor_do_pokemon('clefable'))

# def tipos_do_pokemon(nome):
#     url = f'{site_pokeapi}/api/v2/pokemon/{nome.lower()}/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         list_types = []
#         list = data['types']
#         for i in  list:
#             list_types.append(dic_tipos[i['type']['name']])
#         return list_types
#     # raise PokemonNaoExisteException(Exception)

# print(tipos_do_pokemon('hippowdon'))

# def evolucao_anterior(nome):

#     url = f'{site_pokeapi}/api/v2/pokemon-species/{nome.lower()}'
#     response = requests.get(url)
#     data = response.json()
#     breakpoint()
#     prev_evo = data['evolves_from_species']
#     if prev_evo != None:
#         return prev_evo['name']
#     return None
#         #     PokemonNaoExisteException

# print(evolucao_anterior('charizard'))

def nivel_do_pokemon(nome, experiencia):

        if experiencia < 0: 
            raise ValueError()
        else:
            url = f"{site_pokeapi}/api/v2/pokemon-species/{nome.lower()}/"
            resposta1 = requests.get(url)
            data = resposta1.json()
            url_2 = data['growth_rate']['url']
            resposta2 = requests.get(url_2)
            data_2 = resposta2.json()
            lista_exp = data_2['levels']
            for i in range(0,len(lista_exp)):
                if lista_exp[i]['experience'] <= experiencia and experiencia < lista_exp[i + 1]['experience']:
                    return lista_exp[i]['level']
                else: 
                    return lista_exp[-1]['level']



print(nivel_do_pokemon("togePI",      799999),  99) # 3


def nivel_do_pokemon(nome, experiencia):

    if experiencia < 0: 
        raise ValueError()
    else:
        url = f"{site_pokeapi}/api/v2/pokemon-species/{nome.lower()}/"
        resposta1 = requests.get(url)
        data = resposta1.json()
        url_2 = data['growth_rate']['url']
        resposta2 = requests.get(url_2)
        data_2 = resposta2.json()
        lista_exp = data_2['levels']
        for i in range(0,len(lista_exp)):
            if lista_exp[i]['experience'] >= experiencia:
                if len(str(experiencia)) < 9 and str(experiencia)[-1] == 9:
                    return lista_exp[i]['level']
                elif lista_exp[i]['experience'] == experiencia:
                    return lista_exp[i]['level']
                elif lista_exp[i]['level'] == 100 or lista_exp[i]['experience'] == 0:
                    return i
                else:
                    return i
        return lista_exp[-1]['level']




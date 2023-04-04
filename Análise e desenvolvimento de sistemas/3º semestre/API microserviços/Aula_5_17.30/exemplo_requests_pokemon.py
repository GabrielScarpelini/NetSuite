# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:16:43 2023

@author: Andréia
"""
import requests

# Fazer uma solicitação GET à API do PokéAPI
response = requests.get('https://pokeapi.co/api/v2/pokemon/1/')

# Obter o código de status da resposta
status_code = response.status_code

# Verificar se a solicitação foi bem-sucedida
if status_code == 200:
    # Extrair os dados da resposta JSON
    data = response.json()
    
    # Obter o nome e tipos do Pokémon
    name = data['name']
    types = [t['type']['name'] for t in data['types']]
    
    # Imprimir as informações do Pokémon
    print(f"Name: {name}")
    print(f"Types: {', '.join(types)}")
else:
    print(f"Error: {status_code}")
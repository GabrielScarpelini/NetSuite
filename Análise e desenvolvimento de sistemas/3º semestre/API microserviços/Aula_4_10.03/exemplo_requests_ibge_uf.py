
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:06:24 2023

@author: Andréia
"""


'''
Que tal a API de dados abertos do IBGE? Ela permite acesso a diversos dados estatísticos
 e geográficos do Brasil, sem necessidade de chave de acesso. 
 Aqui está um exemplo de como fazer uma requisição com a API do
 IBGE usando Python e a biblioteca requests:
'''

import requests
from pprint import pprint

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data)
    print(len(data))
else:
    print('Erro na requisição:', response.status_code)

# exemplo_requests_ibge_uf.py
# Exibindo exemplo_requests_ibge_uf.py…'
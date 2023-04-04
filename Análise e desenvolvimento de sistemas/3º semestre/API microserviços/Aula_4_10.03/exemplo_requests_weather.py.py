
import requests
from pprint import pprint

'''
API do OpenWeather, que permite obter informações sobre condições climáticas 
em diferentes cidades do mundo. 
você pode se registrar gratuitamente no site da OpenWeather
 (https://home.openweathermap.org/users/sign_up) para obter uma 
 chave de teste. Depois de se registrar, você pode criar uma nova 
 chave de API em sua conta. A chave de teste gratuita permite fazer
 até 60 solicitações por minuto e 1.000 solicitações por dia.
'''

# Definição da URL da API do OpenWeather
url = 'https://api.openweathermap.org/data/2.5/weather'

# Definição dos parâmetros da consulta (cidade e país)
params = {
    'q': 'São Paulo,BR',
    'appid': 'e658f5d311664546ad48b5087fe78025',
    'units': 'metric'
}

# Envio da solicitação HTTP GET e armazenamento da resposta
response = requests.get(url, params=params)

# Verificação do código de status da resposta
if response.status_code == 200:
    # Processamento dos dados da resposta em formato JSON
    data = response.json()
    # pprint(data)
    
    # Impressão dos dados retornados pela API
    print('Cidade:', data['name'])
    print('País:', data['sys']['country'])
    print('Temperatura:', data['main']['temp'], '°C')
    print('Sensação térmica:', data['main']['feels_like'], '°C')
    print('Descrição:', data['weather'][0]['description'])
else:
    print('Erro na solicitação: código de status', response.status_code)
# exemplo_requests_weather.py
# Exibindo exemplo_requests_weather.py…
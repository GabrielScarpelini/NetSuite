
import requests
from pprint import pprint



if __name__ == '__main__':
    
    cep = '096310 90' #
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    response = requests.get(url)
    '''
    
    # Definição da URL da API do ViaCEP
    url = 'https://viacep.com.br/ws/'


    # Envio da solicitação HTTP GET e armazenamento da resposta
    response = requests.get(url + cep + '/json/')
    '''
    
    if response.status_code == 200:
        data = response.json()

        # Impressão dos dados retornados pela API
        print('CEP:', data['cep'])
        print('Logradouro:', data['logradouro'])
        print('Complemento:', data['complemento'])
        print('Bairro:', data['bairro'])
        print('Localidade:', data['localidade'])
        print('UF:', data['uf'])
    else:
        print('A solicitação falhou com código de status', response.status_code)

# exemplo_requests_cep.py
# Exibindo exemplo_requests_cep.py…
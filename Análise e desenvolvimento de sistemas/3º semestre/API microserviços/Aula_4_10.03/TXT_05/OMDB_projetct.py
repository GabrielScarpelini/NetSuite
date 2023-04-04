import requests
from pprint import pprint

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'


'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
http://www.omdbapi.com/?s=star%20wars&apikey=e51a115c

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
http://www.omdbapi.com/?s=star%20wars&page=2&apikey=e51a115c
'''

'''
Observe que nas URLs acima, estamos passando parâmetros.
'''
api_key = '287da170'
s = 'star wars'
page = 2

def busca_moovies():

    url = f"http://www.omdbapi.com/?i=tt0076759&apikey={api_key}"
    pedido = requests.get(url)

    orders_dic = pedido.json()
    return orders_dic

def busca_por_id(moovie_id):

    url = f"http://www.omdbapi.com/?i=tt0076759&apikey={api_key}&i={moovie_id}"
    pedido = requests.get(url)

    dicionario_do_pedido = pedido.json()

    return dicionario_do_pedido

def busca_por_texto(texto_buscar, page):
    url_p1 = "http://www.omdbapi.com/"
    url_p2 = f"?page={page}&apikey={api_key}&s={texto_buscar}"
    url = url_p1 + url_p2
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido

def busca_qtd_total(texto_buscar):
    lista_texto = busca_por_texto(texto_buscar)
    return len(lista_texto['Search'])

def qnt_filmes(texto_buscar):
    count_moovies = 0
    lista_texto = busca_por_texto(texto_buscar)
    for keys in lista_texto['Search']:
        if keys['Type'] == "movie":
            count_moovies += 1
    return count_moovies    

def qnt_jogos(texto_buscar):
    count_games = 0
    lista_texto = busca_por_texto(texto_buscar)
    for keys in lista_texto['Search']:
        if keys['Type'] == "game":
            count_games += 1
    
    return count_games

# pprint(busca_por_texto('star war'))
# print("total",busca_qtd_total('star war'))
# print('moovies quantity',qnt_filmes('star war'))
# print('games quantity', qnt_jogos('star war'))

'''
Por exemplo, na lista de filmes podemos ver que o filme
star wars original (de 1977) tem id 'tt0076759'

Acessando a URL
http://www.omdbapi.com/?i=tt0076759&apikey={SUA-CHAVE-VEM-AQUI}
podemos ver mais detalhes.

Observe que agora não temos mais o parâmetro 's=star%20wars'
mas sim i=tt0076759. Mudou o nome da "variável", não só
o valor.
'''
# pprint(busca_moovies())
# pprint(busca_por_texto(s, 2))

'''
Faça uma função nome_do_filme_por_id que recebe a id de
um filme e retorna o seu nome.
'''
id_moovie = 'tt0076759'
def nome_do_filme_por_id(id_filme):
    dados = busca_moovies()
    if dados['imdbID'] == id_filme:
        return dados['Title']
    
    return 'ID não localizado'

# print(nome_do_filme_por_id(id_moovie))
'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def ano_do_filme_por_id(id_filme):
    dados = busca_moovies()
    if dados['imdbID'] == id_filme:
        return dados['Released']
    
    return 'ID não localizado'

# print(ano_do_filme_por_id(id_moovie))

'''
Peguemos vários dados de um filme de uma vez.

A ideia é receber uma id e retornar

um dicionário com diversos dados do filme.

O dicionário deve ter as seguintes chaves:
* ano
* nome
* diretor
* genero

E os dados devem ser preenchidos baseado nos dados do site.
'''
def dicionario_do_filme_por_id(id_filme):
    dic_data = {}
    data = busca_moovies()
    if data['imdbID'] == id_filme:
        dic_data['ano'] = ano_do_filme_por_id(id_filme)
        dic_data['nome'] = nome_do_filme_por_id(id_filme)
        dic_data['diretor'] = data['Director']
        dic_data['genero'] = data['Genre']
    return dic_data

# pprint(dicionario_do_filme_por_id(id_moovie))
'''
Voltando para a busca...

Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
def busca_filmes(texto_buscar):
    lista_result = []
    dic = busca_por_texto(texto_buscar)
    lista_dic = dic['Search']
    for i in range(0, 10):
        dic_result = {}
        dic_result['nome'] = lista_dic[i]['Title']
        dic_result['ano'] = lista_dic[i]['Year']
        lista_result.append(dic_result)
    return lista_result

# print(busca_filmes(s))

'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(texto_buscar):
    page = 1
    lista_result = []
    dic = busca_por_texto(texto_buscar, page)
    lista_dic = dic['Search']


    for i in range(0, 20):
        # breakpoint()
        dic = busca_por_texto(texto_buscar, page)
        print(page)
        lista_dic = dic['Search']
        if lista_dic[i]['Type'] == 'movie':
            lista_result.append(lista_dic[i])
        if i == 9:
            page += 1
            i = 0
            print(page)


    # index = 0
    # control = 0

    # while len(lista_result) <= 20:
    #     if control == 9:
    #         page += 1
    #         index = 0
    #         control = 0

    #     dic = busca_por_texto(texto_buscar, page)
    #     lista_dic = dic['Search']

    #     if lista_dic[index]['Type'] == 'movie':
    #         lista_result.append(lista_dic[index])
    #         index += 1
    #         control += 1
    #     else:
    #         index += 1

    return len(lista_result)

# print(busca_filmes_grande(s))

def busca_filmes_grande(texto_buscar):
    dic_busca1 = busca_por_texto(texto_buscar, page=1)
    dic_busca2 = busca_por_texto(texto_buscar, page=2)
    lista_de_filmes1 = dic_busca1['Search']
    lista_de_filmes2 = dic_busca2['Search']
    lista_de_filmes = lista_de_filmes1+lista_de_filmes2
    lista_resposta = []
    for filme in lista_de_filmes:
        dic = {}
        dic['nome'] = filme['Title']
        dic['ano'] = filme['Year']
        dic['tipo'] = filme['Type']
        #guardar o dicionario dic na lista?
        lista_resposta.append(dic)

    return lista_resposta
    
pprint(busca_filmes_grande(s))
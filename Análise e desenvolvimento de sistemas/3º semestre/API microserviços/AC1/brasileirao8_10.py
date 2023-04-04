import json
from pprint import pprint
# -- coding: utf-8 --
'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirao) para estudar como acessar listas,
dicionarios, e estruturas encadeadas (listas dentro de dicionários
dentro de listas)

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor (aperte alt para aparecer o menu,
depois, no canto superior esquerdo, arquivo > "abrir arquivo")

Vale a pena instalar o firefox, porque o leitor de arquivo json dele é muito melhor,
mas também existem extensões pro chrome que fazem a mesma coisa.
'''

'''
DICA VSCODE: para poder executar o arquivo py a partir do VSCODE,
é importante ter aberto a pasta certa

Se voce tem a seguinte estrutura de diretorios
 brasileirao > brasileirao.py
               ano2018.json

Deve selecionar no VSCODE File > Open folder
e escolher a pasta brasileirao.
'''

'''
Se quiser ver os dados dentro do python,
pode chamar a funcao
pega_dados

Nao se preocupe com como ela foi definida, ela só está 
lendo o arquivo json pra voce
'''

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados
dados_br = pega_dados()
#print(dados)
'''
Como você viu nos prints iniciais, cada time tem uma id numérica,
e pode ser acessado em dados['equipes'][id_numerica]

A primeira funcão a fazer recebe a id_numerica de um time e deve retornar 
seu 'nome-comum'

Observe que essa funcão (e todas as demais!) recebem os dados dos
jogos em uma variável dados. Essa variavel  contem todas as informações do arquivo
json que acompanha essa atividade 
'''
def nome_do_time(dados,id_numerica):
    return dados['equipes'][id_numerica]['nome-comum']

'''
A próxima função recebe somente o dicionário dos dados do brasileirao

Ela retorna a id do time que foi campeão.

Lembre-se de usar a variável dados, que foi passada para a função. 
Não use dados2018, a variável global que tinha sido definida antes
'''
def id_campeao(dados):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0]


'''
A proxima funcao recebe somente o dicionario dos dados do brasileirao

Ela retorna o nome-comum do time que foi campeao.
'''
def nome_campeao(dados):
    id_champ = id_campeao(dados)
    return dados['equipes'][id_champ]['nome-comum']

'''
A proxima funcao recebe um tamanho, e retorna uma lista
das ids dos times melhor classificados.

O tamanho da lista que deve ser retornada é o argumento "numero_de_times"
'''
def ids_dos_melhor_classificados(dados,numero_de_times):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0: numero_de_times] #esse [0: numero] já entra nesse range

'''
Façamos agora a busca "ao contrário". Conhecendo o nome-comum de um time, queremos saber sua id.

Se o nome comum nao existir, retorne 'nao encontrado'
'''
def id_do_time(dados,nome_time_procurado):
    for i in dados['equipes']:
        # breakpoint()
        if dados['equipes'][i]['nome-comum'] == nome_time_procurado:
            return i
    return 'Não encontrado'

'''
Crie uma funcao datas_de_jogo, que procura nos dados do brasileirao 
e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirao

dica: busque em dados['fases']

'''
def datas_de_jogo(dados):
    datas = dados['fases']['2700']['jogos']['data'].keys()
    # for i in datas: #esse for retorna exatamente como estava no firefox
    #     if i == {}:
    #         pass
    #     else:
    #         print(f'{i}:')
    return datas

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves sao ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio
'''

def dicionario_id_estadio_e_nro_jogos(dados):
    dic_estadio = {}
    for i in dados['fases']['2700']['jogos']['id']:
        id = dados['fases']['2700']['jogos']['id'][i]['estadio_id']
        if id not in dic_estadio:
            dic_estadio[id] = 1
        else:
            dic_estadio[id] += 1
    # for i in dic_estadio: # tentei ajudar na view nesse for
    #     print(f'id {i} quantidade de jogos {dic_estadio[i]}')
    return dic_estadio


'''
A proxima função recebe (alem do dicionario de dados do brasileirao) uma id de time

Ela retorna a classificacao desse time no campeonato.

Se a id nao for valida, ela retorna a string 'nao encontrado'
'''
def classificacao_do_time_por_id(dados,time_id):
    # classificacao = dados['fases']['2700']['classificacao']['grupo']['Único']
    # if time_id in classificacao:
    #     return classificacao.index(time_id) + 1 
    for i in range(0, len(dados['fases']['2700']['classificacao']['grupo']['Único'])):
        #breakpoint()
        if time_id == int(dados['fases']['2700']['classificacao']['grupo']['Único'][i]):
            return i + 1
    return 'não encontrado'


def dicionario_id_estadio_e_nro_jogo(dados):
    jogos = dados['fases']['2700']['jogos']['id'].values()
    dic_estadio = {jogo['estadio_id']: sum(1 for j in jogos if j['estadio_id'] == jogo['estadio_id']) for jogo in jogos}
    return dic_estadio
# resultado = dicionario_id_estadio_e_nro_jogo(dados_br)
# print(resultado)

if __name__ == '__main__':
    dados2018 = pega_dados()

    '''
    Não dá muito certo imprimir todos os dados, porque o python 
    dá "problema" ao imprimir uma quantidade tao grande de informações, 
    mas podemos ver algumas coisas.

    Descomente cada um dos exemplos abaixo para ver o que ele faz.
    Verifique a correspondencia do que está sendo impresso pelo
    python com o que aparece no firefox

    '''

    # print('Dados do dicionário: ', dados2018)
    # print("\n\n\n") #apenas uns espaços pra te ajudar a ler.

    # print('todas as chaves do dicionario principal', dados2018.keys())


    # print('\n\nEsses foram os dados de todos os times')
    # print('Repare que cada time tem uma id. A id do Flamengo é 1')
    # pprint(dados2018['equipes'])

    # print('\n\nDado do Flamengo')
    # pprint(dados2018['equipes']['1']['nome-comum'])

    # print('\n\nFaixas de classificacao e rebaixamento')
    # pprint(dados2018['fases']['2700']['faixas-classificacao'])

    # print('\n\nClassificacao dos times no fim do campeonato')
    # print(dados2018['fases']['2700']['classificacao']['grupo']['Único'])

    #Aqui, chamar as funções
    # print('Nome do time: ', nome_do_time(dados_br,'15'))
    # print('\nID do campião: ', id_campeao(dados_br))
    # print('\nNome do campeão: ',nome_campeao(dados_br))
    # print('\nLista de ID de 10 melhores: 1st --> 10th',f'{ids_dos_melhor_classificados(dados_br, 10)}\n')
    # print('Id do time tal',id_do_time(dados_br, "Palmeiras"))
    print(f"\nE aqui A lista:\n",datas_de_jogo(dados_br))
    # print(f"\ndicionário: ",dicionario_id_estadio_e_nro_jogos(dados_br))
    print(f'\nPosição {classificacao_do_time_por_id(dados_br,100)}')
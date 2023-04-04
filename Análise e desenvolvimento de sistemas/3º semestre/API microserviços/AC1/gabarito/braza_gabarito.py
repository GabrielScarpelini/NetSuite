import json
from pprint import pprint

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
    id_desejada = id_campeao(dados)
    #toda vez que voce fizer um ctrl-c do seu codigo, lembre-se de que
    # talvez voce podia chamar a funcao e nao copiar e colar
    nome_desejado = nome_do_time(dados,id_desejada)
    return nome_desejado



'''
A proxima funcao recebe um tamanho, e retorna uma lista
das ids dos times melhor classificados.

O tamanho da lista que deve ser retornada é o argumento "numero_de_times"
'''
def ids_dos_melhor_classificados(dados,numero_de_times):
    return dados['fases']['2700']['classificacao']['grupo']['Único'][0:numero_de_times]

'''
Façamos agora a busca "ao contrário". Conhecendo o nome-comum de um time, queremos saber sua id.

Se o nome comum nao existir, retorne 'nao encontrado'
'''
def id_do_time(dados,nome_time_procurado):
   #essa daqui é muito mais dificil, porque transforma nome em id, nao id em nome
   #precisamos olhar todas as ids, olhar o nome correspondente
   dic_equipes = dados['equipes']
   for id_time in dic_equipes.keys(): #as ids sao as chaves do dicionário
       nome_time = (dados['equipes'][id_time]['nome-comum']) #aqui está o nome correspondente
       if nome_time == nome_time_procurado:
           return id_time
   return 'Não encontrado'


'''
Crie uma funcao datas_de_jogo, que procura nos dados do brasileirao 
e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirao

dica: busque em dados['fases']

'''
def datas_de_jogo(dados):
    resposta = []
    for data in dados['fases']['2700']['jogos']['data']:
        resposta.append(data)
    return resposta


'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves sao ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    lista_jogos = dados['fases']['2700']['jogos']['id']
    resposta = {}
    for jogo_id in lista_jogos:
        estadio = lista_jogos[jogo_id]['estadio_id']
        if estadio in resposta:
            resposta[estadio] = resposta[estadio] + 1
        else:
            resposta[estadio] = 1
    return resposta




'''
A proxima função recebe (alem do dicionario de dados do brasileirao) uma id de time

Ela retorna a classificacao desse time no campeonato.

Se a id nao for valida, ela retorna a string 'nao encontrado'
'''
def classificacao_do_time_por_id(dados,time_id):
    classificacao = dados['fases']['2700']['classificacao']['grupo']['Único']
    if time_id in classificacao:
        return classificacao.index(time_id) + 1
    else: return 'Time não encontrado' 


###########################################################################
import unittest

class TestClientes(unittest.TestCase):
    
    def test_001_nome_do_time(self):
        dados = pega_dados()
        self.assertEqual(nome_do_time(dados,'1'),'Flamengo')
        self.assertEqual(nome_do_time(dados,'695'),'Chapecoense')
    
    def test_002_id_campeao(self):
        dados = pega_dados()
        self.assertEqual(id_campeao(dados),'17')
        #assertEqual é tipo um if 
        #verifica se a esquerda é igual a direita, se nao, dá um assertionError
        #e compara os dois

        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(id_campeao(dados),'1')
    
    def test_003_nome_campeao(self):
        dados = pega_dados()
        self.assertEqual(nome_campeao(dados),'Palmeiras')
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(nome_campeao(dados),'Flamengo')
    
   
    def test_004_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados,10),["17","1","15","13","24","4","3","9","5","22"])
        self.assertEqual(ids_dos_melhor_classificados(dados,5),["17","1","15","13","24"])
        self.assertEqual(ids_dos_melhor_classificados(dados,3),["17","1","15"])
 
    
    def test_005_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados,'Cruzeiro'),'9')
        self.assertEqual(id_do_time(dados,'Athletico'),'3')
    
    
    def test_006_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(type(datas),type(["uma" ,"lista"]))
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)


    def test_007_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],16)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id']='72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],17)
    

    def test_008_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados,'17'),1)
        self.assertEqual(classificacao_do_time_por_id(dados,'30'),11)
        self.assertEqual(classificacao_do_time_por_id(dados,'695'),14)
        self.assertEqual(classificacao_do_time_por_id(dados,'1313'),'Time não encontrado')

    
    
    
    
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

#

if __name__ == '__main__':
    dados = pega_dados()
    
        
    print('\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Testes')
    runTests()
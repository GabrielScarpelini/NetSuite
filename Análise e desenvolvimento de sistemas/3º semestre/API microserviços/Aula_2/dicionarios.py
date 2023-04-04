# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:58:57 2023

@author: Andréia
"""


'''
Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.
lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário pode ter as posições 
que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "fabio" e "maria".

(oficialmente, um dicionário não tem "posições", mas sim chaves)
'''

agenda = {}
agenda['marcos']=32112232
agenda['fabio']=988887788
agenda['maria']=44554455 

print("#############################################################")

'''
Crie uma função "consulta" que recebe uma agenda (um dicionário)
e o nome de uma pessoa, e retorna o telefone dessa pessoa
'''

def consulta(agenda, pessoa):
    if pessoa not in agenda:
        return pessoa + " não existe nessa agenda"
    else: 
        return agenda[pessoa]

print(consulta(agenda, 'fabio'))

print("#############################################################")

'''
Crie uma função "adiciona" que recebe uma agenda (um dicionário), o nome de
uma pessoa e um telefone, e adiciona o telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples dicionario['chave'] = valor
'''

def adiciona(agenda,pessoa,telefone):
    if pessoa in agenda:
        return  pessoa + ' Não pode alterar o numero'
    else:
        agenda[pessoa] = telefone
    return agenda

print(adiciona(agenda, 'Gabriel', 966929048))


print("#############################################################")
'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe,
o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario.keys() 
    isso é um teste que retorna True se a chave
    está no dicionário, e False caso contrário.

Temos, por exemplo, os prints seguintes,
que verificam se algumas pessoas estao na agenda
'''
# print('maria esta na agenda?')
# print('maria' in agenda.keys() )

# print('damiao esta na agenda?')
# print('damiao' in agenda.keys() )

# pessoa = 'marcos'
# print('a string da variavel pessoa é uma chave da agenda?')
# print(pessoa in agenda.keys() )

'''
Crie uma função "verifica", que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
'''

def verifica(agenda,pessoa):
    if pessoa in agenda:
        return True
    else:
        return False

print(verifica(agenda, 'Gabriel'))
print("#############################################################")

''' 
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}

'''
Usando seus conhecimentos de dicionário até agora, 
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}

NÃO USE nenhuma função mágica do python. Escreva a lógica
usando dicionários.

O seguinte trecho de código pode ser útil:
>>> palavra='ganancia'
>>> nro_a = 0
>>> for letra in palavra:
	print('estou olhando para',letra)
	if letra == 'a':
		nro_a = nro_a+1

		
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a
>>> nro_a
3
'''

def conta_letras(palavra):
    contagens={}
    for letra in palavra:
        if letra not in contagens:
            contagens[letra] = 1
        else:
            contagens[letra] +=1
    return contagens

print(conta_letras('abacaxi'))
print("#############################################################")


'''
Agora, vamos criar uma agenda um pouco mais completa. 
Dicionário de dicionário. Veja o exemplo
'''

agenda_melhorada= {
        'Andreia': {
            'email': 'andreia.gusmao@faculdadeimpacta.com.br',
            'telefones': [11999999999, 11888888888]
        }, 
        'Maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
        },
        'Arthur': {
            'telefones':[11999999999]     
        }
}


'''
Crie uma função email, que recebe uma agenda (dessas melhoradas)
e uma pessoa.

Ela retorna o email da pessoa. 

Não precisa se preocupar com
o caso do registro da pessoa não ter email (faremos isso
mais pra frente)
'''

def email(agenda_melhorada, pessoa):
    for nome in agenda_melhorada:
        if nome == pessoa:
            return agenda_melhorada[nome]['email']

people = "Andreia"
print(email(agenda_melhorada, people))
print("#############################################################")

# exemplo de for p correr uma lista
# for i in range(0, len(lista)):
#     print(lista[i])

'''
Crie uma função "telefone_principal", que recebe uma agenda 
(nessa versão mais nova) e uma pessoa.

Ela retorna o primeiro telefone da lista de telefones da 
pessoa
'''
def telefone_principal(agenda_melhorada,pessoa):
    return agenda_melhorada[pessoa]['telefones'][0]

print(telefone_principal(agenda_melhorada, 'Andreia'))
print("#############################################################")
'''
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir
>>> for chave in agenda_melhorada.keys():
	print(chave)
Andreia
Maria
Arthur
'''

'''
Crie uma função "sem_email", que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem email.

Por exemplo, sem_email(agenda_melhorada) deve retornar uma
lista com um único contato: ['Arthur']
'''

def sem_email(agenda_melhorada):
    lista_nomes = []
    for nome in agenda_melhorada:
        if 'email' not in agenda_melhorada[nome]:
            lista_nomes.append(nome)

    return lista_nomes

print(sem_email(agenda_melhorada))
print("#############################################################")


##########################################################################

if __name__ == "__main__":
    print('Aqui, chamar as funçoes para teste')

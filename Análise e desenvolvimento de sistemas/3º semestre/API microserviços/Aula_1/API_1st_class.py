texto = 'esse exercicio e um exercicio muito facil ou dificil dificil bagarai'
lista_palavras = texto.split(' ')
ocorrencia = {}

def conta_palavras(text):
    lista_palavras = text.split(' ')
    for palavra in lista_palavras:
        if palavra not in ocorrencia:
                ocorrencia[palavra] = 1
        else:
             ocorrencia[palavra] += 1

    return ocorrencia

print(conta_palavras(texto))
"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)

def total_votos(candidatos):
    total = 0
    for i in range(len(candidatos)):
        votos = int(candidatos[i]['total_votos'])
        total += votos
    return total


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))

def total_votos_por_coligacao(vereadores, coligacoes):
    for i in range(len(vereadores)):
        for j in range(len(coligacoes)):
            if vereadores[i]['coligacao'] == coligacoes[j]['coligacao']:
                votos = int(vereadores[i]['total_votos'])
                coligacoes[j]['qtd_votos'] += votos

def ordem_votacao(vereadores):
    lista = []
    contador = 29
    for i in range(vereadores):




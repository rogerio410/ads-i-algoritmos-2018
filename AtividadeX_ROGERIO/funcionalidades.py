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


def total_votos_validos(vereadores):
    total = reduzir_conjunto(vereadores, 'total_votos', 'soma')
    print('Votos válidos = {}'.format(total))


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def reduzir_conjunto(lista, atributo, operacao='soma'):
    """
    :param lista: lista de dicionários
    :param atributo: chave usada para reduce
    :param operacao: qual operacao utilizada no reduce
    :return:
    """
    acumulado = 0

    for item in lista:
        if operacao == 'soma':
            acumulado += item[atributo]
    return acumulado

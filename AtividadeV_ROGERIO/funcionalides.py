"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total_jogos(jogos):
    print(cabecalho('Total de Jogos'), "Jogos FIFA: {}".format(len(jogos)))


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** FIFA 1930 -- 2014 *****\n'
            ' >> {} <<\n'.format(titulo))

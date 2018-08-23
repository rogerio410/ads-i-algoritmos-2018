"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total_jogos(jogos):
    print(cabecalho('Total de Jogos'), "Jogos FIFA: {}".format(len(jogos)))


def lista_todos_jogos(jogos):
    for jogo in jogos:
        exibir_jogo(jogo)


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** FIFA 1930 -- 2014 *****\n'
            ' >> {} <<\n'.format(titulo))


def exibir_jogo(jogo):
    print(jogo)
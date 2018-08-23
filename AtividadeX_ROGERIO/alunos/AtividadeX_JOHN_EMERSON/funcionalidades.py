"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


from importacao import *

# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def bubble_sort(lista, key=None, reverse=False):
    fim = len(lista)-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(fim):
            a = lista[i]
            b = lista[i + 1]
            if not key:
                if a > b and not reverse or a < b and reverse:
                    swap(lista, i, i + 1)
                    swapped = True
            else:
                if key(a) > key(b) and not reverse or key(a) < key(b) and reverse:
                    swap(lista, i, i + 1)
                    swapped = True
        fim -= 1
    return lista


# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(lista):
    for i in range(len(lista)):
        for j in lista[i]:
            print(j + ':', lista[i][j])
        print()


def total_de_votos_validos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += int(lista[i]['total_votos'])
    return soma


def quociente_eleitoral(total_votos, vagas):
    return total_votos // vagas


def add_votos_por_coligacao(coligacoes):
    for i in range(len(coligacoes)):
        coligacao = coligacoes[i]['coligacao']
        total = 0
        vereadores = importar_vereadores('candidatos_e_votos_vereador_THE_2012.csv')
        for j in range(len(vereadores)):
            if vereadores[j]['coligacao'] == coligacao:
                total += int(vereadores[j]['total_votos'])
        coligacoes[i]['total_votos'] = total


def total_de_vagas(coligacoes):
    for i in range(len(coligacoes)):
        coligacao = coligacoes[i]['coligacao']
        vagas = coligacoes[i]['qtd_vagas']
        print('Coligacao:', coligacao)
        print('Total de vagas(por QP):', vagas)
        print('Total de votos sobra:', coligacoes[i]['votos_sobra_total'])
        print()


def imprimir_votos_por_coligacao(coligacoes):
    for i in range(len(coligacoes)):
        print('Coligacao:', coligacoes[i]['coligacao'])
        print('Total de votos:', coligacoes[i]['total_votos'])
        print()


def add_vagas_e_sobras(coligacoes, QE):
    for i in range(len(coligacoes)):
        votos = coligacoes[i]['total_votos']
        QP = votos // QE
        coligacoes[i]['qtd_vagas'] = QP
        sobras = votos / (QP + 1)
        coligacoes[i]['votos_sobra_total'] = sobras


def imprimir_vereadores_mais_votados(vereadores):
    lista = []
    for i in range(len(vereadores)):
        linha = [vereadores[i]['nome'], int(vereadores[i]['total_votos'])]
        lista.append(linha)

    bubble_sort(lista, key=lambda x: x[1], reverse=True)

    for j in range(len(lista)):
        if j == 29:
            break
        else:
            print('{}º candidato eleito:'.format(j+1), lista[j][0])
            print('Total de votos:', lista[j][1])
            print()


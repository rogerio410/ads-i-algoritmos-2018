"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total_votos(candidatos):
    somatorio_votos = 0
    for linha in candidatos:
        somatorio_votos += linha['total_votos']
    return somatorio_votos


def quociente_eleitoral(candidatos, vagas=29):
    return total_votos(candidatos) // vagas


def total_votos_por_coligacao(candidatos, coligacoes):
    for linha_col in coligacoes:
        somatorio = 0
        for linha_can in candidatos:
            if linha_col['coligacao'] == linha_can['coligacao']:
                somatorio += linha_can['total_votos']
        linha_col['total_votos'] = somatorio


def quantidade_de_vagas(candidatos, coligacoes):
    total_votos_por_coligacao(candidatos, coligacoes)
    quociente = quociente_eleitoral(candidatos)
    for linha in coligacoes:
        linha['qtd_vagas'] = linha['total_votos']//quociente


def quantidade_de_sobras(candidatos, coligacoes):
    total_votos_por_coligacao(candidatos, coligacoes)
    quociente = quociente_eleitoral(candidatos)
    for linha in coligacoes:
        linha['votos_sobra_total'] = linha['total_votos'] % quociente

def vagas_de_sobra_final(candidatos, coligacoes, vagas=29):
    quantidade_de_vagas(candidatos, coligacoes)
    quantidade_de_sobras(candidatos, coligacoes)
    vagas_preenchidas = 0
    for linha in coligacoes:
        vagas_preenchidas += linha['qtd_vagas']
    if vagas > vagas_preenchidas:
        while vagas_preenchidas != vagas:
            maior_calculo = calculo_de_vagas(coligacoes)
            coligacoes[maior_calculo]['qtd_vagas'] += 1
            vagas_preenchidas += 1


def imprimir_vereadores_eleitos(candidatos, coligacoes):
    vagas_de_sobra_final(candidatos, coligacoes)
    eleitos = []
    for linha in coligacoes:
        eleitos_coligacao = top_vagas_coligacao(linha['qtd_vagas'], candidatos)
        for eleito in eleitos_coligacao:
            eleitos.append(eleito)
    print('-' * 120)
    indice = 1
    for eleito in eleitos:
        print('{}º - Nome do Candidato: {} | Nome do partido: {} | Total de Votos: {}'.
              format(indice, eleito['nome'], eleito['partido'],eleito['total_votos']))
        print('-' * 120)
        indice += 1



# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('\n***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))

def imprimir_coligacoes_e_total_voltos(coligacoes):
    print('-' * 60)
    for linha in range(len(coligacoes)):
        print('{}º - Coligação: {} | Total de Votos: {}'.format(linha + 1, coligacoes[linha]['coligacao'],
                                                            coligacoes[linha]['total_votos']))
        print('-' * 60)


def imprimir_coligacoes_qtd_vagas_qtd_sobras(coligacoes):
    print('-' * 75)
    for linha in range(len(coligacoes)):
        print('{}º - Coligação: {} | Quantidade de Vagas: {} | Quantidade de Sobras: {}'.
              format(linha + 1, coligacoes[linha]['coligacao'], coligacoes[linha]['qtd_vagas'],
                     coligacoes[linha]['votos_sobra_total']))
        print('-' * 75)

def calculo_de_vagas(coligacoes):
    maior = 0
    for linha in range(len(coligacoes)):
        if coligacoes[linha]['total_votos']//(coligacoes[linha]['qtd_vagas'] + 1) > \
                coligacoes[maior]['total_votos']//(coligacoes[maior]['qtd_vagas'] + 1):
            maior = linha
    return maior


def imprimir_vagas(coligacoes):
    print('-' * 75)
    for linha in range(len(coligacoes)):
        print('{}º - Coligação: {} | Quantidade de Vagas: {}'.
              format(linha + 1, coligacoes[linha]['coligacao'], coligacoes[linha]['qtd_vagas']))
        print('-' * 75)


def top_vagas_coligacao(vagas, candidatos):
    coligacao_aux = list(candidatos)
    bubble_sort(coligacao_aux, inverso=True, chave=lambda x: x['total_votos'])
    return top_n(coligacao_aux, vagas)


def troca(lista, elemento1, elemento2):
    lista_a_aux = lista[elemento1]
    lista[elemento1] = lista[elemento2]
    lista[elemento2] = lista_a_aux


def maior_que(elemento1, elemento2):
    return elemento1 > elemento2


def menor_que(elemento1, elemento2):
    return elemento1 < elemento2


def bubble_sort(lista, inverso=False, chave=lambda x: x):
    trocou = True
    fim = len(lista)-1
    operacao = maior_que
    if inverso:
        operacao = menor_que
    while trocou:
        trocou = False
        for indice in range(0, fim):
            if operacao(chave(lista[indice]), chave(lista[indice + 1])):
                trocou = True
                troca(lista, indice, indice + 1)
        fim -= 1


def top_n(lista, n):
    lista_top = []
    for linha in range(n):
        lista_top.append(lista[linha])
    return lista_top



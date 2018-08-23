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


def total_de_votos_validos(vereadores):
    total = 0
    for vereador in vereadores:
        total += vereador['total_votos']

    return total


def quociente_eleitoral(total_votos, vagas):
    return total_votos // vagas


def total_de_votos_coligacao(vereadores, coligacao):
    for vereador in vereadores:
        for colig in coligacao:
            if vereador['coligacao'] in colig['coligacao']:
                colig['total_votos'] += vereador['total_votos']
                continue


def total_de_vagas_por_coligacao(coligacao, qe, vagas):
    resto = vagas

    for dado in coligacao:
        if resto == 0:
            break
        vagas = dado['total_votos'] // qe
        if (resto - vagas) < 0:
            vagas = resto
        dado['qtd_vagas'] = vagas
        resto -= vagas

    for dado in coligacao:
        dado['votos_sobra_total'] = dado['total_votos'] / (dado['qtd_vagas'] + 1)

    return resto


def vagas_de_sobra(coligacoes, sobra):
    while sobra > 0:
        posicao = 0

        for caligacao in range(len(coligacoes)):
            if coligacoes[caligacao]['votos_sobra_total'] > coligacoes[posicao]['votos_sobra_total']:
                posicao = caligacao

        coligacoes[posicao]['qtd_vagas'] += 1


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def selection_sort(dados, reverse=False, key=None):
    inicio = 0
    fim = len(dados)

    while inicio < fim:
        selecionado = 0
        if not key:
            for i in range(len(dados)):
                if not reverse and dados[i] < dados[selecionado]:
                    selecionado = i
                elif reverse and dados[i] > dados[selecionado]:
                    selecionado = i
            swap(dados, inicio, selecionado)
        else:
            for i in range(len(dados)):
                if not reverse and key(dados[i]) < key(dados[selecionado]):
                    selecionado = i
                elif reverse and key(dados[i]) > key(dados[selecionado]):
                    selecionado = i
            swap(dados, inicio, selecionado)

        inicio += 1


def ordenar_dicionario(dados):
    inicio = 0
    fim = len(dados)

    while inicio < fim:
        selecionado = 0
        for i in range(inicio, fim):
            if dados[i]['total_votos'] > dados[selecionado]['total_votos']:
                selecionado = i
        swap(dados, inicio, selecionado)
        inicio += 1


def swap(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

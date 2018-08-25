# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)


def somar_votos_dos_meus_vereadores(coligacao, vereadores):
    soma = 0
    for vereador in vereadores:
        if vereador['coligacao'] == coligacao:
            soma += vereador['total_votos']
    return soma


def calcular_vagas_por_QP(coligacoes, quociente_eleitoral):
    total_vagas_distribuidas = 0
    for coligacao in coligacoes:
        coligacao['qtd_vagas'] = coligacao['total_votos'] // quociente_eleitoral
        total_vagas_distribuidas += coligacao['qtd_vagas']
    return total_vagas_distribuidas


def calcular_vagas_por_media(coligacoes, vagas_sobrantes):

    while vagas_sobrantes > 0:
        for coligacao in coligacoes:
            coligacao['media'] = coligacao['total_votos'] / (coligacao['qtd_vagas'] + 1)

        bubble_sort(coligacoes, chave=lambda x:x['media'], inverso=True)

        coligacoes[0]['qtd_vagas'] += 1
        vagas_sobrantes -= 1


def marcar_os_eleitos_para_cada_coligacao(coligacoes, vereadores):

    for coligacao in coligacoes:
        meus_vereadores = filtrar_por_atributo(vereadores, 'coligacao', coligacao['coligacao'])
        bubble_sort(meus_vereadores, chave=lambda x:x['total_votos'], inverso=True)
        for vereador in meus_vereadores[0:coligacao['qtd_vagas']]:
            vereador['eleito'] = True


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def reduzir_por_atributo_e_operacao(lista, atributo, operacao):
    acumulado = 0
    for item in lista:
        if operacao == '+':
            acumulado += item[atributo]
    return acumulado


def filtrar_por_atributo(lista, atributo, valor_atributo):
    sub_conjunto = []
    for item in lista:
        if item[atributo] == valor_atributo:
            sub_conjunto.append(item)
    return sub_conjunto


def bubble_sort(dados, chave=None, inverso=False):

    trocou = True
    fim = len(dados) - 1

    while trocou:
        trocou = False
        for i in range(fim):
            item_esquerda = dados[i]
            item_direita = dados[i+1]

            esquerda_maior = item_esquerda > item_direita if chave is None else chave(item_esquerda) > chave(item_direita)
            esquerda_menor = item_esquerda < item_direita if chave is None else chave(item_esquerda) < chave(item_direita)

            if (not inverso and esquerda_maior) or (inverso and esquerda_menor):
                trocar(dados, i, item_direita, item_esquerda)
                trocou = True

        fim -= 1


def trocar(dados, i, item_direita, item_esquerda):
    aux = item_esquerda
    dados[i] = item_direita
    dados[i + 1] = aux

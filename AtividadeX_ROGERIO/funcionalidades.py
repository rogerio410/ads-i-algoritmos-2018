# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)


def total_votos_validos(vereadores):
    total = reduzir_conjunto(vereadores, 'total_votos', 'soma')
    return total


def atualizar_votos_sobra_total(coligacoes):
    for coligacao in coligacoes:
        coligacao['votos_sobra_total'] = coligacao['total_votos'] // (coligacao['qtd_vagas'] + 1)


def calcular_qtd_vagas_por_quociente_eleitoral(coligacoes, qtd_vagas, quociente_eleitoral):
    vagas_distribuidas = 0
    for coligacao in coligacoes:
        coligacao['qtd_vagas'] = int(coligacao['total_votos'] // quociente_eleitoral)
        coligacao['votos_sobra_total'] = coligacao['total_votos'] // (coligacao['qtd_vagas'] + 1)
        vagas_distribuidas += coligacao['qtd_vagas']

    return qtd_vagas - vagas_distribuidas


def calcular_qtd_vagas_por_media(coligacoes, qtd_vagas_sobra):
    while qtd_vagas_sobra > 0:
        bubble_sort(coligacoes, chave=lambda x:x['votos_sobra_total'], inverso=True)
        coligacoes[0]['qtd_vagas'] += 1
        atualizar_votos_sobra_total(coligacoes)
        qtd_vagas_sobra -= 1


def marca_vereadores_eleitos(coligacoes, vereadores):

    for coligacao in coligacoes:
        vereadores_coligacao = filtrar_conjunto(vereadores, 'coligacao', coligacao['coligacao'])
        bubble_sort(vereadores_coligacao, chave=lambda x:x['total_votos'], inverso=True)
        vereadores_coligacao_eleitos = vereadores_coligacao[:coligacao['qtd_vagas']]
        for vereador in vereadores_coligacao_eleitos:
            vereador['eleito'] = True


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def reduzir_conjunto(lista, atributo, operacao='soma'):

    acumulado = 0
    for item in lista:
        if operacao == 'soma':
            acumulado += item[atributo]
    return acumulado


def filtrar_conjunto(lista, atributo, valor_atributo):

    selecionados = []
    for item in lista:
        if item[atributo] == valor_atributo:
            selecionados.append(item)
    return selecionados


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
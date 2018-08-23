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
        print(registro['coligacao'], registro['total_votos'])


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def votos_validos(vereadores):
    soma = 0
    for i in range(len(vereadores)):
        voto = int(vereadores[i]['total_votos'])
        soma += voto
    print(soma, 'votos validos')


def quociente_eleitoral(vereadores):
    soma = 0
    for i in range(len(vereadores)):
        voto = int(vereadores[i]['total_votos'])
        soma += voto
    quociente = soma // 29
    print('Quociente Eleitoral =', quociente)


def total_votos_coligacao(vereadores, coligacoes):
    for i in range(len(coligacoes)):
        soma_votos_colicao = 0
        coligacao = coligacoes[i]['coligacao']
        for j in range(len(vereadores)):
            if coligacao == vereadores[j]['coligacao']:
                soma_votos_colicao += int(vereadores[j]['total_votos'])
        coligacoes[i]['total_votos'] = soma_votos_colicao
        print(coligacao, 'possue', soma_votos_colicao, 'votos')


def total_de_vagas(coligacoes, vereadores):
    soma = 0
    for i in range(len(vereadores)):
        voto = int(vereadores[i]['total_votos'])
        soma += voto
    quociente = soma // 29
    soma_vagas = 0
    maior = 0
    for j in range(len(coligacoes)):
        coligacao = coligacoes[j]
        votos_coligacao = coligacoes[j]['total_votos']
        qp = votos_coligacao // quociente
        sobra = votos_coligacao // (qp + 1)
        soma_vagas += qp
        coligacao['qtd_vagas'] = qp
        if qp > 0:
            sobra_votos = votos_coligacao % quociente
            coligacao['votos_sobra_total'] = sobra_votos
        print(coligacao['coligacao'], ',vagas >', coligacao['qtd_vagas'], ',Sobra de votos >',
              coligacao['votos_sobra_total'])
    resta_vagas = 29 - soma_vagas
    print('Restaram', resta_vagas, 'vagas')


def vereadores_eleitos(vereadores):
    copia_vereadores = [] + vereadores
    nova_lista = []
    posicao = 0
    copia = [] + vereadores
    aux = []
    posicao = 0
    while len(aux) != len(vereadores):
        maior = 0
        for i in range(len(copia)):
            if int(copia[i]['total_votos']) > maior:
                maior = int(copia[i]['total_votos'])
                linha_maior = copia[i]
                posicao = i
        aux.append(linha_maior)
        copia[posicao] = {'total_votos': 0}
    print(aux)
    for k in range(29):
        print(aux[k]['nome'],aux[k] ['numero'],aux[k] ['partido'],aux[k] ['coligacao'], aux[k]['total_votos'])


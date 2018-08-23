"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open('partidos_coligacoes_the_2012.csv', 'r')

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip())

    return registros


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open('candidatos_e_votos_vereador_THE_2012.csv', 'r')

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip().split(';'))

    return registros

def show_afonso(lista):
    for i in lista:
        print(i)

def total_votos(lista):
    soma = 0
    for i in range(len(lista)):
        soma += int(lista[i]['total_votos'])
    print('O número total de votos validos é %d'%soma)


def quociente_eleitoral(lista):
    soma = 0
    for i in range(len(lista)):
        soma += int(lista[i]['total_votos'])

    calculo = soma/29
    print('O Quociente Eleitoral é %.0f'%calculo)


def total_votos_coligacoes(coligacoes, vereadores):
    lista = []
    for vereador in vereadores:
        for coligacao in coligacoes:
            if vereador["coligacao"] == coligacao["coligacao"]:
                coligacao["total_votos"] += vereador["total_votos"]

    show_afonso(coligacoes)


def total_vagas_partidario(coligacoes):
    soma = 1
    for coligacao in coligacoes:
        coligacao['qtd_vagas'] += (coligacao['total_votos']//13631)
        if coligacao['total_votos'] < 13631:
            soma += 1
    show_afonso(coligacoes)
    print('Vagas que sobraram: ', soma)






"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip())

    return registros


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip().split(';'))

    return registros

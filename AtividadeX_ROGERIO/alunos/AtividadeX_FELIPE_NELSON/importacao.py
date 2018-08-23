"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    coligacoes =[]
    for linha in arquivo.readlines():
        linha_limpa = linha.strip()
        dicionario = {}
        dicionario['coligacao'] = linha_limpa
        dicionario['total_votos'], dicionario['qtd_vagas'], dicionario['votos_sobra_total'] = 0, 0, 0
        coligacoes.append(dicionario)

    return coligacoes


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    vereadores = []
    for linha in arquivo.readlines():
        linha_limpa = linha.strip()
        dicionario = {}
        linha_em_lista = linha_limpa.split(';')
        dicionario['nome'] = linha_em_lista[0]
        dicionario['numero'] = linha_em_lista[1]
        dicionario['partido'] = linha_em_lista[2]
        dicionario['coligacao'] = linha_em_lista[3]
        dicionario['total_votos'] = linha_em_lista[4]
        vereadores.append(dicionario)
    converter_dados_inteiros(vereadores)
    return vereadores


def converter_dados_inteiros(matriz):
    for linha in matriz:
        for coluna in linha:
            if coluna == 'numero' or coluna == 'total_votos':
                linha[coluna] = int(linha[coluna])

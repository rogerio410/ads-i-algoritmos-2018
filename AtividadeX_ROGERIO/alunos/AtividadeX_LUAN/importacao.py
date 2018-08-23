"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        linsta_nova = linha.strip()
        dicionario = {}
        
        dicionario['coligacao'] = linsta_nova
        dicionario['total_votos'] = 0
        dicionario['qtd_vagas'] = 0
        dicionario['votos_sobra_total'] = 0 

        registros.append(dicionario)

    return registros


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():

        dicionario = {}
        vereadores = linha.strip().split(';')
        
        dicionario['nome'] = vereadores[0]
        dicionario['numero'] = int(vereadores[1])
        dicionario['partido'] = vereadores[2]
        dicionario['coligacao'] = vereadores[3]
        dicionario['total_votos'] = int(vereadores[4])
        dicionario['eleito'] = False

        registros.append(dicionario)

    return registros


def transformar_coluna_para_int(vereador, coluna):
    vereador[coluna] = int(vereador[coluna])


def total_votos(coligacoes, vereadores):
    for coligacao in coligacoes:
        for candidato in vereadores:
            if candidato['coligacao'] == coligacao['coligacao']:
                coligacao['total_votos'] += candidato['total_votos']



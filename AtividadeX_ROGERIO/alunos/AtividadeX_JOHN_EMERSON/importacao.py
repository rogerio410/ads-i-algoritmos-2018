"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo1 = open(arquivo)
    partidos_e_coligacoes = []
    coligacoes = []

    for linhas in arquivo1:
        linha = linhas.strip()
        partidos_e_coligacoes.append(linha)

    for j in partidos_e_coligacoes:
        coligacao = {'coligacao': j, 'total_votos': 0, 'qtd_vagas': 0, 'votos_sobra_total': 0}
        coligacoes.append(coligacao)

    return coligacoes


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo2 = open(arquivo)
    todos_candidatos = []
    candidatos = []

    for item in arquivo2:
        itens = item.strip().split(';')
        todos_candidatos.append(itens)

    for k in range(len(todos_candidatos)):
        candidato = {'nome': todos_candidatos[k][0], 'numero': todos_candidatos[k][1],
                     'partido': todos_candidatos[k][2], 'coligacao': todos_candidatos[k][3],
                     'total_votos': todos_candidatos[k][4]}
        candidatos.append(candidato)

    return candidatos

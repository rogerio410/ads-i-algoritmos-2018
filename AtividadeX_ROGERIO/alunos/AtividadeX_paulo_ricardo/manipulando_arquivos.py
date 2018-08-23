def arquivo1():
    arq1 = open('partidos_coligacoes_the_2012.csv', 'r')
    lista_coligacoes = []
    for linha in arq1:
        dicio_coligacao = {}
        linha = linha[:-1]
        dicio_coligacao['coligacao'] = linha
        dicio_coligacao['total_votos'] = 0
        dicio_coligacao['qtd_vagas'] = 0
        dicio_coligacao['votos_sobra_total'] = 0
        lista_coligacoes.append(dicio_coligacao)

    return lista_coligacoes


def arquivo2():
    arq2 = open('candidatos_e_votos_vereador_THE_2012.csv', 'r')
    lista_candidatos = []
    for linha in arq2:
        dicio_candidatos = {}
        linha = linha.split(';')
        linha[-1] = linha[-1][:-1]
        dicio_candidatos['nome'] = linha[0]
        dicio_candidatos['numero'] = int(linha[1])
        dicio_candidatos['partido'] = linha[2]
        dicio_candidatos['coligacao'] = linha[3]
        dicio_candidatos['total_votos'] = int(linha[4])
        lista_candidatos.append(dicio_candidatos)

    return lista_candidatos


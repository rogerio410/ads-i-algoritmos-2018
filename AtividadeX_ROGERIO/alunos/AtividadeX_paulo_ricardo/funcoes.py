from manipulando_arquivos import *


def somatoria_total_votos(candidatos):
    total = 0

    for dicio_linha in candidatos:
        total += dicio_linha['total_votos']

    return total


def cociente_eleitoral(total_votos):
    vagas = 29

    return total_votos // vagas


def total_votos_coligacoes(candidatos, coligacoes):
    for i in range(len(coligacoes)):
        total = 0
        dicio_coli = coligacoes[i]
        coligacao = dicio_coli['coligacao']

        for j in range(len(candidatos)):
            dicio_cand = candidatos[j]
            coligacao_candidato = dicio_cand['coligacao']
            if coligacao == coligacao_candidato:
                total += dicio_cand['total_votos']
        coligacoes[i]['total_votos'] = total
    for i in range(len(coligacoes)):
        dicio_coligacao = coligacoes[i]
        print('{}: {}'.format(dicio_coligacao['coligacao'], dicio_coligacao['total_votos']))

    return coligacoes


def total_vagas_por_conciente(coligacoes, candidatos):
    todos_votos = somatoria_total_votos(candidatos)
    minimo_voto_por_vaga = cociente_eleitoral(todos_votos)
    for i in range(len(coligacoes)):
        dicio_coligacoes = coligacoes[i]
        total_votos = dicio_coligacoes['total_votos']
        quant_vagas = total_votos // minimo_voto_por_vaga
        dicio_coligacoes['qtd_vagas'] = quant_vagas
        sobra_votos = total_votos % minimo_voto_por_vaga
        dicio_coligacoes['votos_sobra_total'] = sobra_votos
        coligacoes[i] = dicio_coligacoes

    for i in range(len(coligacoes)):
        dicio_coligacao = coligacoes[i]
        print('{} tem {} vagas, sobraram {} votos'.format(dicio_coligacao['coligacao'],
                                                          dicio_coligacao['qtd_vagas'],
                                                          dicio_coligacao['votos_sobra_total']))

    return coligacoes


def distribuindo_resto_vagas(coligacoes):
    lista_votos_sobrando = []
    vagas_usados = 0
    vagas = 29
    for i in range(len(coligacoes)):
        dicio_coligacoes = coligacoes[i]
        lista_votos_sobrando.append(dicio_coligacoes['votos_sobra_total'])
        vagas_usados += dicio_coligacoes['qtd_vagas']

    vagas_sobraram = vagas - vagas_usados

    for i in range(vagas_sobraram):
        maior = 0
        p = 0
        for j in range(len(lista_votos_sobrando)):
            if maior < lista_votos_sobrando[j]:
                maior = lista_votos_sobrando[j]
                p = j
        del lista_votos_sobrando[p]

        for k in range(len(coligacoes)):
            dicio_coligacoes = coligacoes[k]
            if maior == dicio_coligacoes['votos_sobra_total']:
                dicio_coligacoes['qtd_vagas'] += 1

    for i in range(len(coligacoes)):
        dicio_coligacao = coligacoes[i]
        print('{} tem {} vagas, sobraram {} votos'.format(dicio_coligacao['coligacao'],
                                                          dicio_coligacao['qtd_vagas'],
                                                          dicio_coligacao['votos_sobra_total']))

    return coligacoes


def eleitos(coligacoes, candidatos):
    contador = 0
    for i in range(len(coligacoes)):
        lista_quat_votos_cand_da_coligacao = []
        dicio_coligacao = coligacoes[i]
        coligacao = dicio_coligacao['coligacao']
        for j in range(len(candidatos)):
            dicio_candidato = candidatos[j]
            coligacao_cand = dicio_candidato['coligacao']
            if coligacao_cand == coligacao:
                quant_votos_cand = dicio_candidato['total_votos']
                lista_quat_votos_cand_da_coligacao.append(quant_votos_cand)

        quant_vagas = dicio_coligacao['qtd_vagas']
        for j in range(quant_vagas):
            maior = 0
            p = 0

            for k in range(len(lista_quat_votos_cand_da_coligacao)):
                if maior < lista_quat_votos_cand_da_coligacao[k]:
                    maior = lista_quat_votos_cand_da_coligacao[k]
                    p = k
            del lista_quat_votos_cand_da_coligacao[p]

            for x in range(len(candidatos)):
                dicio_candidato = candidatos[x]
                if dicio_candidato['total_votos'] == maior:
                    show_dados(dicio_candidato)
                    contador += 1

def show_dados(dicio):
    print('')
    for chave in dicio:
        print('{}: {}'.format(chave, dicio[chave]))


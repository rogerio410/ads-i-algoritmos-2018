"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####
from select_sort import select_sort

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)


def listar_coligacoes(coligacoes):
	for item in coligacoes:
		print(item["coligacao"])


def total_votos_validos(candidatos):
	total = votos_validos(candidatos) 

	print(cabecalho('Total de votos válidos'), "{}".format(total))


def quociente_eleitoral(candidatos):
	quociente = qe(candidatos) 
	print(cabecalho('Quociente eleitoral'), "{}".format(quociente))


def total_votos_coligacao(coligacoes, candidatos):
	for coligacao in coligacoes:
		regra = lambda candidato: candidato["coligacao"] == coligacao["coligacao"]

		candidatos_da_coligacao = filtrar_por_regra(candidatos, regra=regra)

		total_coligacao = somar(candidatos_da_coligacao, key=lambda candidato: candidato["total_votos"])
		
		coligacao["total_votos"] = total_coligacao


def vagas_por_qp(coligacoes, candidatos):
	quociente = qe(candidatos)

	for coligacao in coligacoes:
		coligacao["qtd_vagas"] = coligacao["total_votos"] // quociente
		coligacao["votos_sobra_total"] = coligacao["total_votos"] % quociente

	total_qtd_vagas = somar(coligacoes, key=lambda coligacao: coligacao["qtd_vagas"])

	vagas_restantes = 29 - total_qtd_vagas

	print(cabecalho('Vagas restantes'), "{}".format(vagas_restantes))


def eleitos_nao_proporcional(candidatos):
	eleitos = candidatos[:29]

	for eleito in eleitos:
		print(eleito["nome"])


def percentual_partidos(candidatos):
	validos = votos_validos(candidatos)

	partidos = [candidato["partido"] for candidato in candidatos]

	partidos = list(set(partidos))

	registros = []

	for partido in partidos:
		candidatos_do_partido = filtrar_por_regra(candidatos, regra=lambda candidato: candidato["partido"] == partido)
		total_votos = somar(candidatos_do_partido, key=lambda candidato: candidato["total_votos"])
		percentual = (total_votos/validos) * 100

		registros.append({"partido": partido, "total_votos": total_votos, "percentual": percentual})

	ordenar_por(registros, "percentual", reverse=True)

	exibir_partidos(registros)


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def ordenar_por(matriz, atributo, reverse=False):
    select_sort(matriz, key=lambda x: x[atributo], reverse=reverse)


def somar(conjunto, key=lambda x: x):
	somatorio = 0

	for item in conjunto:
		somatorio += key(item)

	return somatorio


def filtrar_por_regra(lista, regra):
    return [elemento for elemento in lista if regra(elemento)]


def exibir_coligacoes(coligacoes):
	for coligacao in coligacoes:
		print("Coligação: %s" % (coligacao["coligacao"]))
		print("Votos: %d" % (coligacao["total_votos"]))
		print()


def exibir_partidos(registros):
	for partido in registros:
		print("Partido: %s" % (partido["partido"]))
		print("Percentual de votos: %.2f %%" % (partido["percentual"]))
		print()


def votos_validos(candidatos):
	return somar(candidatos, key=lambda candidato: candidato["total_votos"])


def qe(candidatos):
	return somar(candidatos, key=lambda candidato: candidato["total_votos"]) // 29
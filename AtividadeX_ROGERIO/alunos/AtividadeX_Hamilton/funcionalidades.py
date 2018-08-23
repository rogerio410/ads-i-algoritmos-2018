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
        print(registro["coligacao"])


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def total_de_votos(vereadores):
	total = 0
	for item in vereadores:
		total += int(item['total_votos'])
	print('Total de Votos Válidos:', total)

def total_de_votos_validos(vereadores):
	total = 0
	for item in vereadores:
		total += int(item['total_votos'])
	return total

def quociente_eleitoral(vereadores):
	votos = total_de_votos_validos(vereadores)
	quociente = votos//29
	return quociente

def voto_por_coligacao(Coligacoes, vereadores):
	for dic in Coligacoes:
		for d in vereadores:
			if dic['coligacao'] == d['coligacao']:
				dic['total_votos'] += int(d['total_votos'])
	return Coligacoes

def atualizar_qtd_vagas(coligacoes, vereadores):
	voto_por_coligacao(coligacoes, vereadores)
	quociente = quociente_eleitoral(vereadores)
	for dic in coligacoes:
		total = dic['total_votos']
		vagas = total//quociente
		dic['qtd_vagas'] += vagas
		if vagas != 0:
			dic['votos_sobra_total'] = (total//vagas) + 1
	return coligacoes
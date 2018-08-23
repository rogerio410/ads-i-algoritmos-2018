"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    print(cabecalho('Coligações'))
    for registro in dados:
    	print(registro['coligacao'])


def somatorio_atributo(dados, atributo):
	total = 0
	for registro in dados:
		total += registro[atributo]
	return total


def coeficiente_eleitoral(coligacoes):
	total_votos = somatorio_atributo(coligacoes, 'total_votos')

	return total_votos / 29


def total_votos_coligacao(conjunto, atributo):
	print(cabecalho('Total de %s por coligação' %atributo))
	for registro in conjunto:
		print ('%s : %d' %(registro['coligacao'], registro[atributo]))


def total_vagas(coligacoes):
	print(cabecalho('Total de vagas por coligação'))
	coeficiente = coeficiente_eleitoral(coligacoes)
	for registro in coligacoes:
		registro['qnt_vagas'] = registro['total_votos'] // coeficiente
	
	soma = 0
	for i in coligacoes:
		soma += i['qnt_vagas']
	sobras = 29 - soma	

	for i in range(5):
		for registro in coligacoes:
			registro['votos_sobra_total'] = registro['total_votos'] / (registro['qnt_vagas'] + 1)

		bubble_sort(coligacoes, key= lambda x: x['votos_sobra_total'])

		for i in range(len(coligacoes)):
			if i == 0:
				coligacoes[i]['qnt_vagas'] += 1
				break

	for registro in coligacoes:
		print('%s : %d' %(registro['coligacao'], registro['qnt_vagas']))

	print('Quantidade de vagas restantes: %d' %sobras)



def imprimir_lista_vereadores_aprovador(coligacoes, vereadores):
	bubble_sort(vereadores, reverse=True, key = lambda x: x['total_votos'])
	lista_eleito = []

	for registro in coligacoes:
		qnt_eleito = registro['qnt_vagas']

		for candidato in vereadores:
			if registro['coligacao'] == candidato['coligacao']:
					lista_eleito.append(candidato['nome'])
			if qnt_eleito == 0:
				break

	print(cabecalho('Cadidatos Eleitos'))
	for candidato in lista_eleito:
		print(candidato)





# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def bubble_sort(lista, key = lambda x: x, reverse = False):
    fim = len(lista) - 1

    trocou = True
    while trocou:
        trocou = False

        for i in range(fim):

            if (not reverse and key(lista[i]) > key(lista[i + 1])) \
                or (reverse and key(lista[i]) < key(lista[i + 1])):
                    swap(lista, i + 1, i)
                    trocou = True
        fim -= 1

def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def elitos(vereadores):
	for candidato in vereadores:
		candidato['eleito'] = False





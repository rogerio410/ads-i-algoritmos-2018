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
        print(registro)


def votos_validos(vereadores):
	cont_votos = 0
	for i in range(len(vereadores)):
		cont_votos += vereadores[i][4]

	print("Total de votos validos: ", cont_votos)

	return cont_votos


def quociente_eleitoral(vereadores, vagas=29):
	cont_votos = 0
	for i in range(len(vereadores)):
		cont_votos += vereadores[i][4]

	quociente = cont_votos / vagas

	print("quociente eleitoral: %.2f" % quociente)

	return quociente


def total_votos_por_coligacao(coligacoes):
	for i in range(len(coligacoes)):
		print("Coligaão: %s..........Total de votos: %d" % (coligacoes[i][0], coligacoes[i][1]))

	return coligacoes


def lista_eleitos_eleicao_nao_proporcional(vereadores):
	vereadores = plinio_sort(vereadores, key=por_votos, reverse=True)

	for i in range(29):
		print("%d - %s , %d votos" % (i+1, vereadores[i][0], vereadores[i][4]))


def percentual_votos_cada_partido(vereadores):
	'''# 1. Ordenar por partidos
	vereadores = plinio_sort(vereadores, key=por_partido)

	# 2. Listar partidos
	aux = []
	for i in range(len(vereadores)):
		if i == 0:
			partido = vereadores[i][2]
			aux.append(partido)
		else:
			if vereadores[i][2] != partido:
				partido = vereadores[i][2]
				aux.append(partido)
	partido = aux

	for i in range(len(partido)):
		partido[i] = [partido[i]]


	for i in range(len(partido)):
		soma = 0
		for j in range(len(vereadores)):
			if(partido[i] == vereadores[j][2]):
				soma = soma + vereadores[j][4]
		partido[i].append(soma)

	for i in range(len(partido)):
		print(partido[i])'''
		
	print("Em breve!")



# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))

def transforma_inteiro(matriz):
	for i in range(len(matriz)):
		matriz[i][4] = int(matriz[i][4])

	return matriz

def add_total_votos_cada_coligacao(coligacoes, vereadores):
	for i in range(len(coligacoes)):
		cont = 0
		for j in range(len(vereadores)):
			if(coligacoes[i] == vereadores[j][3]):
				cont = cont + vereadores[j][4]

		coligacoes[i] = [coligacoes[i]]
		coligacoes[i].append(cont)

	return coligacoes

def plinio_sort(lista, key=None, reverse=False):
	inicio = 0
	fim = len(lista)-1

	while(inicio < fim):
		maior = inicio
		menor = inicio

		for i in range(inicio+1, fim+1):
			if key(lista[i]) < key(lista[menor]):
				menor = i

			if key(lista[i]) > key(lista[maior]):
				maior = i

		if reverse:
			if menor == inicio:
				menor = maior

			lista[inicio], lista[maior] = lista[maior], lista[inicio]
			lista[fim], lista[menor] = lista[menor], lista[fim]
			
		else:
			if maior == inicio:
				maior = menor

			lista[inicio], lista[menor] = lista[menor], lista[inicio]
			lista[fim], lista[maior] = lista[maior], lista[fim]

		inicio += 1
		fim -= 1

	return lista

def por_partido(vereadores):
	return vereadores[2]

def por_votos(vereadores):
	return vereadores[4]

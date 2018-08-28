"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total_jogos(jogos):
    print(cabecalho('Total de Jogos'), "Jogos FIFA: {}".format(len(jogos)))


def jogos_selecao_especifica(matriz_dados):
	print(cabecalho('Jogos de uma seleção especifica'))
	
	nome = input("Nome da seleção: ")

	lista = []
	for i in range(851):
		if(nome == matriz_dados[i][5]) or (nome == matriz_dados[i][8]):
			lista.append(matriz_dados[i])

	for i in range(len(lista)):
		print(lista[i])


def jogos_por_parte_nome(matriz_dados):
	print(cabecalho('Jogos de uma seleção por parte do nome'))
	
	nome = input("Digite: ")

	lista = []
	for i in range(851):
		if((nome in matriz_dados[i][5].upper()) or (nome in matriz_dados[i][5].lower())) or ((nome in matriz_dados[i][8].upper()) or (nome in matriz_dados[i][8].lower())):
			lista.append(matriz_dados[i])

	for i in range(len(lista)):
		print(lista[i])	

def jogos_de_final(matriz_dados):
	print(cabecalho('Jogos de final'))

	lista = []
	for i in range(851):
		if(matriz_dados[i][2] == 'Final'):
			lista.append(matriz_dados[i])

	for i in range(len(lista)):
		print(lista[i])
	


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis


def cabecalho(titulo):
    return ('***** FIFA 1930 -- 2014 *****\n'
            ' >> {} <<\n'.format(titulo))

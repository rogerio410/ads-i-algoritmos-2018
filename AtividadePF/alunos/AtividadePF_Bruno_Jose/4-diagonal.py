def main():
    nome_input = input("Digite um nome: ").split()
    nome = juntar_string(nome_input)
    imprimir_matriz(nome)


def imprimir_matriz(nome):
	vetor = []
	matriz_aux = []

	for i in range(len(nome)):
		vetor.append(nome[i])

	for j in range(len(nome)):
		matriz = []
		for l in range(len(nome)):
			matriz.append("-")
		matriz_aux.append(matriz)

	for i in range(len(matriz_aux)):
		for j in range(len(matriz_aux[i])):
			if i == j:
				matriz_aux[i][j] = vetor[i]

	for i in range(len(matriz_aux)):
		print(matriz_aux[i])
        

def juntar_string(nome_recebido):
    s = ""
    for i in range(len(nome_recebido)):
        s += nome_recebido[i]
    return s
        


if __name__ == '__main__':
    main()

def main():
	nome = input("Digiete um nome: ")
	tam = len(nome)

	matriz = nova_matriz(tam, tam, '-')

	aux = 0
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if(i == j):
				matriz[i][j] = nome[aux]
				aux = aux+1

	for i in range(len(matriz)):
		for j in range(len(matriz)):
			print(matriz[i][j], end=' ')
		print()

def nova_matriz(linhas, colunas, valor = None):
    matriz = [None] * linhas

    for i in range(len(matriz)):
        matriz[i] = [valor] * colunas
    
    return matriz
if __name__ == '__main__':
    main()


def main():
	nome = input("Digiete um nome: ")

	matriz = [['-'] * len(nome)] * len(nome)

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
if __name__ == '__main__':
    main()
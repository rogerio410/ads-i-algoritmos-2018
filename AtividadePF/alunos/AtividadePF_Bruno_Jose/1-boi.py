def main():
    num_fichas = int(input("Digite o numero de fichas de controle da sua boiada: "))

    menor, maior, media = controle_boiada(num_fichas)

    exibicao(num_fichas, menor, maior, media)


def controle_boiada(num_fichas):
	matriz_de_controle = [[0]] * num_fichas
	vetor_peso = []
	media_peso = 0

	for i in range(len(matriz_de_controle)):
		for j in range(len(matriz_de_controle[i])):
			numero_identificao = int(input("Digite o numero de identifição: "))
			peso = float(input("Digite o peso do boi em KG: "))
			vetor_peso.append(peso)
			matriz_de_controle[i] = [numero_identificao, peso]
			media_peso += matriz_de_controle[i][1]
	maior_peso, menor_peso = peso_maior_e_menor(vetor_peso)
	print(maior_peso, menor_peso)
	
	return menor_peso, maior_peso, media_peso


def peso_maior_e_menor(vetor):
    maior = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    menor = vetor[0]
    for j in range(len(vetor)):
        if vetor[j] < menor:
            menor = vetor[j]
    return maior, menor


def exibicao(num_fichas, menor, maior, media):
	print("Peso do menor boi: %.1f" % menor)
	print("Peso do maior boi: %.1f" % maior)
	print("Media de peso dos bois: %.1f" % media)
	print("Quantidade de bois: %d" % num_fichas)


if __name__ == '__main__':
    main()

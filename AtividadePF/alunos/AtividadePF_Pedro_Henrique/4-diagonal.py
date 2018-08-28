def main():
    nome = input('Digite o nome: ')
    matriz = make_matriz(len(nome))
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = nome[contador]
                contador += 1

    mostra_matriz(matriz)


def make_matriz(n):
    matriz = []

    for i in range(n):
        aux = []
        for j in range(n):
            aux.append('-')
        matriz.append(aux)

    return matriz


def mostra_matriz(matriz):
    for item in matriz:
        print(item)


if __name__ == '__main__':
    main()

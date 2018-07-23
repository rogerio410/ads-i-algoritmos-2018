def main():
    n =  int(input())

    while n != 0:
        matriz = nova_matriz(n, n, None)
        preencher_matriz(matriz, n)
        show(matriz)
        print()
        n = int(input())


def preencher_matriz(matriz, n):

    for i in range(n):
        for j in range(n):
            if i == j:
                matriz[i][j] = 1
            elif j < i:
                # matriz[i][j] = '*'
                # valor atual é igual a valor de cima(i-1) somado com 1
                matriz[i][j] = matriz[i-1][j] + 1
            elif j > i:  # poderia ser apenas else.
                # matriz[i][j] = '#'
                # valor atual é igual ao valor da esquerda(j -1) somado com 1
                matriz[i][j] = matriz[i][j-1] + 1


def nova_matriz(linhas, colunas, valor=None):
    matriz = [None] * linhas
    for i in range(len(matriz)):
        matriz[i] = [valor] * colunas
    return matriz


def show(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            item = str(matriz[i][j]).rjust(3)
            if j < len(matriz) - 1:
                item += ' '
            print(item, end='')
        print()


if __name__ == '__main__':
    main()
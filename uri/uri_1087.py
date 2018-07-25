
def main():
    i, j, x, y = list(map(int,input().split()))

    while i != 0 and j != 0 and x != 0 and y != 0:
        if mesma_casa(i, j, x, y):
            print(0)
        elif mesma_linha(i, x) \
                or mesma_coluna(j, y) \
                or mesma_diagonal(i, j, x, y):
            print(1)
        else:
            print(2)

        i, j, x, y = list(map(int, input().split()))










def mesma_casa(i, j, x, y):
    return i == x and j == y


def mesma_linha(i, x):
    return i == x


def mesma_coluna(j, y):
    return j == y


def mesma_diagonal(i, j, x, y):
    return i + j == x + y or j - i == y - x


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
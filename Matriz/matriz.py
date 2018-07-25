def nova_matriz(linhas, colunas, valor=None):
    matriz = [None] * linhas
    for i in range(len(matriz)):
        matriz[i] = [valor] * colunas
    return matriz


def nova_matriz_quadrada(ordem, valor=None):
    return nova_matriz(ordem, ordem, valor)


def alinhar(valor, tam, lado='d'):
    valor = str(valor)
    espacos = ' ' * (tam - len(valor))
    if lado == 'd':
        return espacos+valor
    elif lado == 'e':
        raise ValueError('Em desenvolvimento')


def show(matriz, pad=5):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            item = alinhar(matriz[i][j], pad)
            if j < len(matriz) - 1:
                item += ' '
            print(item, end='')
        print()
        print()


def na_diagonal_principal(i, j):
    return i == j


def mudar_valor_diag_principal(matriz, valor):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if na_diagonal_principal(i, j):
                matriz[i][j] = valor


def acima_diagonal_principal(i, j):
    return i < j


def abaixo_diagonal_principal(i, j):
    return i > j


def na_diagonal_secundaria(i, j, tamanho_matriz):
    return i + j == tamanho_matriz -1


def acima_diagonal_secundaria(i, j, tamanho_matriz):
    return i + j < tamanho_matriz - 1


def abaixo_diagonal_secundaria(i, j, tamanho_matriz):
    return i + j > tamanho_matriz - 1


def mesma_casa(i, j, x, y):
    return i == x and j == y


def mesma_linha(i, x):
    return i == x


def mesma_coluna(j, y):
    return j == y


def mesma_diagonal(i, j, x, y):
    return i + j == x + y or j - i == y - x

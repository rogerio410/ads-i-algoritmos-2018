import time


DESCER, IR_ESQ, IR_DIR = 'b', 'e', 'd'
MAX_NULOS = 0
MAX_NEGATIVOS = 0
memoria = {}


def main():
    global MAX_NULOS
    global MAX_NEGATIVOS
    global memoria

    # receber parametros
    qtd_linhas, qtd_colunas, MAX_NULOS, MAX_NEGATIVOS = list(map(int, input().split()))
    # criar e povoar matriz
    #matriz = nova_matriz(qtd_linhas, qtd_colunas)
    matriz = nova_matriz_dict(qtd_linhas, qtd_colunas)
    receber_dados(matriz,qtd_colunas, qtd_linhas)

    # ir de 0,0 até n,n
    memoria = nova_matriz_dict(qtd_linhas, qtd_colunas, None)
    for i in range(len(memoria)):
        for j in range(len(memoria[i])):
            memoria[i][j] = {}
    inicio = time.time()
    custo= navegar(matriz)
    custo = 'Impossivel' if custo == 99999999999999 else custo
    print(custo)
    print('{:.6f}s'.format((time.time() - inicio)))


def navegar(matriz, qtd_nulos=0, qtd_negativos=0, i=0, j=0, origem='ESQ'):
    global memoria

    # custo 'infinito'
    infinito = 99999999999999
    c1, c2, c3 = infinito, infinito, infinito

    atual = matriz[i][j]

    if atual < 0:
        qtd_negativos += 1

    if atual == 0:
        qtd_nulos += 1

    if i == 0 and j == 0 and MAX_NEGATIVOS == 0 and atual < 0:
        return infinito
    if i == 0 and j == 0 and MAX_NULOS == 0 and atual == 0:
        return infinito

    if i == (len(matriz)-1) and j == (len(matriz[i])-1):
        return atual

    if origem == 'ESQ':
        # descer ou ir a direita
        if pode(DESCER, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, DESCER)
            if key in memoria[i][j]:
                c1 = memoria[i][j].get(key)
            else:
                c1 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i+1, j, 'CIMA')
                memoria[i][j][key] = c1

        if pode(IR_DIR, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, IR_DIR)
            if key in memoria[i][j]:
                c2 = memoria[i][j].get(key)
            else:
                c2 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i, j + 1, 'ESQ')
                memoria[i][j][key] = c2

    elif origem == 'CIMA':
        # ir as esquerda ou direita
        if pode(DESCER, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, DESCER)
            if key in memoria[i][j]:
                c1 = memoria[i][j].get(key)
            else:
                c1 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i + 1, j, 'CIMA')
                memoria[i][j][key] = c1

        if pode(IR_DIR, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, IR_DIR)
            if key in memoria[i][j]:
                c2 = memoria[i][j].get(key)
            else:
                c2 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i, j + 1, 'ESQ')
                memoria[i][j][key] = c2

        if pode(IR_ESQ, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, IR_ESQ)
            if key in memoria[i][j]:
                c3 = memoria[i][j].get(key)
            else:
                c3 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i, j - 1, 'DIR')
                memoria[i][j][key] = c3

    else:  # origem == 'DIR'
        # ir a esquerda ou descer
        if pode(DESCER, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, DESCER)
            if key in memoria[i][j]:
                c1 = memoria[i][j].get(key)
            else:
                c1 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i + 1, j, 'CIMA')
                memoria[i][j][key] = c1

        if pode(IR_ESQ, i, j, matriz, qtd_nulos, qtd_negativos):
            key = '{}-{}-{}'.format(qtd_nulos, qtd_negativos, IR_ESQ)
            if key in memoria[i][j]:
                c3 = memoria[i][j].get(key)
            else:
                c3 = atual + navegar(matriz, qtd_nulos, qtd_negativos, i, j - 1, 'DIR')
                memoria[i][j][key] = c3

    # retornar menor custo
    menor_custo = min(c1, c2, c3)
    #print('Menor Custo', menor_custo)
    return menor_custo


def pode(direcao, i, j, matriz, qtd_nulos, qtd_negativos):

    if direcao == DESCER:
        if i < (len(matriz) - 1):
            if qtd_nulos >= MAX_NULOS and matriz[i + 1][j] == 0:
                return False
            if qtd_negativos >= MAX_NEGATIVOS and matriz[i + 1][j] < 0:
                return False
            return True
        else:
            return False

    if direcao == IR_ESQ:
        if j > 0:
            if qtd_nulos >= MAX_NULOS and matriz[i][j-1] == 0:
                return False
            if qtd_negativos >= MAX_NEGATIVOS and matriz[i][j-1] < 0:
                return False
            return True
        else:
            return False

    if direcao == IR_DIR:
        if j < (len(matriz[i]) - 1):
            if qtd_nulos >= MAX_NULOS and matriz[i][j+1] == 0:
                return False
            if qtd_negativos >= MAX_NEGATIVOS and matriz[i][j+1] < 0:
                return False
            return True
        else:
            return False


def receber_dados(matriz, qtd_colunas, qtd_linhas):
    for i in range(qtd_linhas):
        numeros = list(map(int, input().split()))
        for j in range(qtd_colunas):
            matriz[i][j] = numeros[j]


def nova_matriz(linhas, colunas, valor=None):
    matriz = [None] * linhas
    for i in range(len(matriz)):
        matriz[i] = [valor] * colunas
    return matriz


def nova_matriz_dict(linhas, colunas, valor=None):
    matriz = {}
    for i in range(linhas):
        matriz[i] = {}
        for j in range(colunas):
            matriz[i][j] = valor
    return matriz


def show(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def main2():
    while True:
        # main()
        try:
            main()
        except EOFError:
            break


if __name__ == '__main__':
    main2()
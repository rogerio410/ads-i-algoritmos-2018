
def main():
    n =  int(input())

    while n != 0:
        matriz = nova_matriz(n, n, '*')
        preecher_matriz(matriz)
        show(matriz)
        print()
        n = int(input())


def preecher_matriz(matriz):
    inicio = 0
    fim = len(matriz)
    valor = 1

    while inicio < fim:
        preencher_extremidade(inicio, fim, matriz, valor)
        inicio += 1
        fim -= 1
        valor += 1


def preencher_extremidade(inicio, fim, matriz, valor):
    for i in range(inicio, fim):
        for j in range(inicio, fim):
            if extremidade(i, j, inicio, fim):
                matriz[i][j] = valor


def extremidade(i, j, inicio, fim):
    if i == inicio or j == fim-1 or i == fim-1 or j == inicio:
        return True


def nova_matriz(linhas, colunas, valor=None):
    matriz = [None] * linhas
    for i in range(len(matriz)):
        matriz[i] = [valor] * colunas
    return matriz


def show(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            #item = str(matriz[i][j]).rjust(3)
            item = justificar(matriz[i][j], 3)
            if j < len(matriz) - 1:
                item += ' '
            print(item, end='')
        print()


def justificar(valor, tam, lado='d'):
    valor = str(valor)
    espacos = ' ' * (tam - len(valor))
    if lado == 'd':
        return espacos+valor
    elif lado == 'e':
        return valor+espacos


if __name__ == '__main__':
    main()
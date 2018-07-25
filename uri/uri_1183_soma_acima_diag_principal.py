def main():

    # nova matriz de ordem 12
    matriz = [0] * 12
    for i in range(len(matriz)):
        matriz[i] = [0] * 12

    op = input()

    # receber dados
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = float(input())

    somatorio = 0.0
    contador = 0
    # filtrar e somar os elementos da Diag. Principal
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                somatorio += matriz[i][j]
                contador += 1


    # soma ou media
    if op == 'S':
        print(somatorio)
    else:
        print('%.1f' % (somatorio/contador))
        #print('{:.1f}'.format(somatorio/contador))


    # show matriz
    # for i in range(len(matriz)):
    #     print(matriz[i])

if __name__ == '__main__':
    main()
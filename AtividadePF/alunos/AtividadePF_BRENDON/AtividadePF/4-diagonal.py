def main():

    nome = input('Digite um nome:')
    matriz(nome)


def matriz(nome):

    linha = ['-'] * len(nome)
    for i in range(len(nome)):
        matriz = [linha] * len(linha)
    matriz[1][1] = 'w'
    print(matriz)




if __name__ == '__main__':
    main()
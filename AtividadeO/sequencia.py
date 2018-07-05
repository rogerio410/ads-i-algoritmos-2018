def main():
    soma = 0
    soma_positivos = 0
    soma_negativos = 0
    #for i in range(10000, 0, -1):
    for i in range(1, 10000):
        numerador = 1
        if i % 2 == 0:
            denominador = -i
        else:
            denominador = i

        elemento = numerador / denominador

        if elemento > 0:
            soma_positivos += elemento
        else:
            soma_negativos += elemento

        soma += elemento

    print('A: ', soma)
    print('C positivos: ', soma_positivos)
    print('C negativos : ', soma_negativos)
    print('C: ', soma_negativos + soma_positivos)


if __name__ == '__main__':
    main()
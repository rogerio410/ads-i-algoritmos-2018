def main():

    numerador = 1
    somatorio = 0.0

    for denominador in range(1, 51):
        #print("%d/%d" %(numerador, denominador), end=' ')
        somatorio = somatorio + (numerador / denominador)
        numerador += 2

    print('Resultado = %.2f' % somatorio)

if __name__ == '__main__':
    main()
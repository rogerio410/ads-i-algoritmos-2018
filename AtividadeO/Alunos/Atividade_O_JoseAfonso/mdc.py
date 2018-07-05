def main():

    #entrada
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    #processamento
    while numero_2 != 0:
        resto = numero_1 % numero_2
        numero_1 = numero_2
        numero_2 = resto

    #saída
    print('O MDC dos números escolhidos equivale a {}'.format(numero_1))

if __name__ == '__main__':
    main()
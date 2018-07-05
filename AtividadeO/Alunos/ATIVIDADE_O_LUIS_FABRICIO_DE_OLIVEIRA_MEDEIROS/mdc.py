def main():

    # entrada
    numero1 = int(input('N1: '))
    numero2 = int(input('N2: '))

    # processamento
    while numero2 != 0:
        temporario = numero2
        numero2 = numero1 % numero2
        numero1 = temporario

    # saida
    print('Resultado: {}'.format(numero1))


if __name__ == '__main__':
    main()

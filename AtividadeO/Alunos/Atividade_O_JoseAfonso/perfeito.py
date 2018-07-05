def main():

    #entrada
    numero = int(input('Digite um número: '))
    numero_escolhido = numero

    #processamento
    soma = 0
    for i in range(1, numero + 1):

        if numero % i == 0:
            soma = soma + i

    #saída
    if (soma - numero_escolhido) == numero:
        print('{} é um número perfeito'.format(numero))

    else:
        print('{} não é um número perfeito'.format(numero))


if __name__ == '__main__':
    main()


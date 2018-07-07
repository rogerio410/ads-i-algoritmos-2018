def main():
    # Apresentação
    print('Esse programa verifica se um número é perfeito.')

    # Entradas
    numero = int(input('Digite um número: '))

    # Processamento
    soma = 0
    for i in range(1, numero): #Verifica cada possibidade de divisão
        if numero % i == 0:
            soma += i

    # Saída
    if soma == numero:
        print('{} é número perfeito.'.format(numero))
    else:
        print('{} não é um número perfeito.'.format(numero))


if __name__ == '__main__':
    main()

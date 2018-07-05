def main():
    # entrada
    n = int(input('Digite o número:'))

    # processamento
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    # saidas
    if soma == n:
        print('Perfeito.')
    else:
        print('Não é perfeito.')


if __name__ == '__main__':
    main()

def main():
    # entrada
    n = int(input('Digite o numero: '))

    # processamento
    divisores = 0

    for i in range(1, n):
        if n % i == 0:
            divisores += i

    # saida
    if divisores == n:
        print('{} eh perfeito'.format(n))
    else:
        print('{} nao eh perfeito'.format(n))


if __name__ == '__main__':
    main()

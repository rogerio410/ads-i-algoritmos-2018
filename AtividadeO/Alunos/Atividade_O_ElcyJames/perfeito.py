def main():
    n = int(input('Número: '))
    divisores = 0
    aux = n - 1
    while aux > 0:
        if n % aux == 0:
            divisores += aux
        aux -= 1
    if divisores == n:
        print('Perfeito')
    else:
        print('Não é perfeito')


if __name__ == '__main__':
    main()
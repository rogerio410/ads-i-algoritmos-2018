def main():

    # entrada
    numero = int(input())
    divisores = 0

    # processamento
    for i in range(1, numero):
        if numero % i == 0:
            divisores += i
        else:
            continue
    # saida
    if divisores == numero:
        print('Perfeito')
    else:
        print('Não é perfeito')


if __name__ == '__main__':
    main()
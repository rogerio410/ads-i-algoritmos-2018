def main():
    # entrada
    numero = int(input())

    # processamento
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    # saida
    if soma == numero:
        print("{} é perfeito." .format(numero))
    else:
        print("{} não é perfeito." .format(numero))


if __name__ == '__main__':
    main()

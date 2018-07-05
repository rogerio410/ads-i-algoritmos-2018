def main():
    numero = int(input('Digite um inteiro: '))

    for n in range(1, numero):
        if eh_perfeito(n):
            print(n)


def eh_perfeito(numero):
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i

    if soma_divisores == numero:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
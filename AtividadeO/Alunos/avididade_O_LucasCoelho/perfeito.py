def main():

    n = int(input())

    perfeito = eh_perfeito(n)

    if perfeito:
        print('É perfeito')
    else:
        print('Não é perfeito')


def eh_perfeito(valor):
    resultado = 0

    for n in range(1, valor):
        if valor % n == 0:
            resultado += n

        if resultado == valor:
            return True

    return False


if __name__=='__main__':
    main()


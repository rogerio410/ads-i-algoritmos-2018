def main():
    # Entrada
    n = int(input("Forneça um número inteiro positivo: "))
    print()

    # Processamento
    perfeito = eh_perfeito(n)

    # Saída
    if perfeito:
        print("%d é perfeito" % (n))

    else:
        print("%d não é perfeito" % (n))


def eh_perfeito(n):
    """ Retorna True se 'n' for um número perfeito."""
    soma = 0

    for i in range(n-1, 0, -1):
        if soma > n:
            return False

        if eh_divisor(i, n):
            soma += i

    return soma == n


def eh_divisor(n1, n2):
    """ Retorna True se 'n1' for divisor de 'n2'."""
    return n2 % n1 == 0


if __name__ == "__main__":
    main()

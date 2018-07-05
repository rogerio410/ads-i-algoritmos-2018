def main():
    # Entrada
    n1 = int(input("Forneça dois números inteiros positivos: "))
    n2 = int(input())

    # Processamento e saída
    print("\nMDC = %d" % (mdc(n1, n2)))


def mdc(n1, n2):
    while n2 != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto

    return n1


if __name__ == "__main__":
    main()

def main():
    # Processamento e saída
    a = sequencia_a()
    b = sequencia_b()
    c = sequencia_c()
    d = sequencia_d()

    print("Sequência 'a':", a)
    print("Sequência 'b':", b)
    print("Sequência 'c':", c)
    print("Sequência 'd':", d)
    print()

    if a == b == c == d:
        print("Retornam os mesmos valores")

    else:
        print("Não retornam os mesmos valores")


def sequencia_a():
    """ Adição da esquerda para a direita"""
    resultado = 0

    for i in range(1, 10001):
        resultado += 1/i

    return resultado


def sequencia_b():
    """ Adição da direita para a esquerda"""
    resultado = 0

    for i in range(10000, 0, -1):
        resultado += 1/i

    return resultado


def sequencia_c():
    """ Positivos e negativos da esquerda para a direita"""
    resultado = 0

    denominador = 1

    while denominador < 10000:
        resultado += 1/denominador

        denominador += 1

        resultado -= 1/denominador

        denominador += 1

    return resultado


def sequencia_d():
    """ Positivos e negativos da direita para a esquerda"""
    resultado = 0

    denominador = 10000

    while denominador > 0:
        resultado += 1/denominador

        denominador -= 1

        resultado -= 1/denominador

        denominador -= 1

    return resultado


if __name__ == "__main__":
    main()

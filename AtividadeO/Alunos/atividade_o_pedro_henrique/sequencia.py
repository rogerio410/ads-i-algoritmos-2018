def main():
    a = adicao_esquerda_direita()
    b = adicao_direita_esquerda()
    c = separacao_termos_esq_dir()
    d = separacao_termos_dir_esq()

    if a == b == c == d:
        print('Todas retornam os mesmos valores')
    else:
        print('Nao retornam os mesmos valores')


def adicao_direita_esquerda():
    num = 1
    resultado = 0

    for i in range(2, 10001):
        if i % 2 == 0:
            resultado = resultado - (1 / i)
        else:
            resultado = resultado + (1 / i)

    resultado = num - resultado

    return resultado


def adicao_esquerda_direita():
    num = 1
    resultado = 0

    for i in range(10001, 1):
        if i % 2 == 0:
            resultado = resultado - (1 / i)
        else:
            resultado = resultado + (1 / i)

    resultado = num - resultado

    return resultado


def separacao_termos_esq_dir():
    num = 1
    positivos = 0
    negativos = 0

    for i in range(2, 10001):
        if i % 2 == 0:
            negativos = negativos + (1 / i)
        else:
            positivos = positivos + (1 / i)

    resultado = num - (positivos - negativos)

    return resultado


def separacao_termos_dir_esq():
    num = 1
    positivos = 0
    negativos = 0

    for i in range(10000, 1):
        if i % 2 == 0:
            negativos = negativos + (1 / i)
        else:
            positivos = positivos + (1 / i)

    resultado = num - (positivos - negativos)

    return resultado


if __name__ == '__main__':
    main()

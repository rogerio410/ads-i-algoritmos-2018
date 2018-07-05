# Adição da Esquerda para a Direita
def a():
    # contador
    soma = 0

    # processamento
    for i in range(1, 1001):
        if i % 2 == 0:
            soma += -(1 / i)
        else:
            soma += 1 / i

    # retorno
    return soma


# Adição da Direita para a Esquerda
def b():
    # contador
    soma2 = 0

    # processamento
    for i in range(1000, 0, -1):
        if i % 2 == 0:
            soma2 += -(1 / i)
        else:
            soma2 += 1 / i

    # retorno
    return soma2


# Separação dos termos positivos e negativos da Esquerda para a Direita
def c():
    # contadores
    soma3_positivos = 0
    soma3_negativos = 0

    # processamento
    for i in range(1, 1001):
        if i % 2 == 0:
            soma3_negativos += -(1 / i)
        else:
            soma3_positivos += 1 / i

    # retorno
    return soma3_positivos + soma3_negativos


# Separação dos termos positivos e negativos da Direita para a Esquerda
def d():
    # contadores
    soma4_positivos = 0
    soma4_negativos = 0

    # processamento
    for i in range(1000, 0, -1):
        if i % 2 == 0:
            soma4_negativos += -(1 / i)
        else:
            soma4_positivos += 1 / i

    # retorno
    return soma4_positivos + soma4_negativos


def main():
    # processamento
    if a() == b() == c() == d():
        #saida
        print('Retornam o mesmo valor!')
    else:
        #saida
        print('Não retorna o mesmo valor!')


if __name__ == '__main__':
    main()

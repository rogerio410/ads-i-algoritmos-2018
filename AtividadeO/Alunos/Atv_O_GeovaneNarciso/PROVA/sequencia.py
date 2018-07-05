def main():
    # entrada

    # processamento

    # saida
    print("a) ", soma_esq_a_dir())
    print("b)", soma_dir_a_esq())
    print("c)", pos_e_neg_dir_a_esq())
    print("d)", pos_e_neg_esq_a_dir())


def soma_esq_a_dir():
    soma_a = 0
    for i in range(1, 10001, 2):
        soma_a += (1 / i) - (1 / (i + 1))

    return soma_a


def soma_dir_a_esq():
    soma_b = 0
    for i in range(10000, 0, -2):
        soma_b += (1 / i) - (1 / (i - 1))

    return soma_b


def pos_e_neg_esq_a_dir():
    soma_c = 0
    soma_pos = 0
    soma_neg = 0
    for i in range(1, 10001, 2):
        soma_pos += (1 / i) + (1 / (i + 2))
    for i in range(1, 10001, 2):
        soma_neg += (1 / (i + 1)) + (1 / (i + 3))
    soma_c = soma_pos - soma_neg

    return soma_c


def pos_e_neg_dir_a_esq():
    soma_d = 0
    soma_pos = 0
    soma_neg = 0
    for i in range(1000, 4, -2):
            soma_pos += (1 / i) + (1 / (i - 2))
    for i in range(10000, 4, -2):
            soma_neg += (1 / (i - 1)) + (1 / (i - 3))
    soma_d = soma_pos - soma_neg

    return soma_d


if __name__ == '__main__':
    main()

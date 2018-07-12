def main():

    qtd_itens = int(input('Qtd Elementos?'))

    vetor = [None] * qtd_itens
    vetor_somas_acumuladas = [None] * qtd_itens

    obter_numeros(vetor)
    #cumsum(vetor, vetor_somas_acumuladas)

    #vetor_chop = [None] * (len(vetor) - 2)
    #chop(vetor, vetor_chop)

    #print(vetor_somas_acumuladas)
    #print(vetor_chop)

    #vetor_middle = middle(vetor)

    #print(vetor_middle)

    ordenado = is_sorted(vetor)

    print('ORDENADO: ', 'SIM' if ordenado else 'NAO')


def obter_numeros(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input('Item %d: ' % i))


def cumsum(vetor1, vetor2):
    soma = 0
    for i in range(len(vetor1)):
        soma += vetor1[i]
        vetor2[i] = soma


def chop(vetor, resultado):
    for i in range(1, len(vetor)-1):
        resultado[i - 1] = vetor[i]


def middle(vetor):
    result = list(vetor)

    while len(result) > 2:
        v_chop = [None] * (len(result) - 2)
        chop(result, v_chop)
        result = v_chop

    return result


def is_sorted(vetor):
    for i in range(1, len(vetor)):
        item_atual = vetor[i]
        item_anterior = vetor[i-1]

        if item_atual < item_anterior:
            return False
    return True


if __name__ == '__main__':
    main()
def main():

    n = int(input('Qtd de Sublista? '))

    vetor = [None] * n

    print(vetor)
    obter_dados(vetor)
    print(vetor)
    converter_para_inteiro(vetor)
    print(vetor)

    soma = nested_sum(vetor)

    print('Soma Valores: ', soma)


def obter_dados(vetor):
    for i in range(len(vetor)):
        entrada = input('Digite e a lista: ')
        sublista = entrada.split()
        vetor[i] = sublista


def converter_para_inteiro(lista):
    # operacao de Mapeamento (MAP)
    for i in range(len(lista)):
        lista[i] = list(map(int, lista[i]))
        # for j in range(len(lista[i])):
        #     lista[i][j] = int(lista[i][j])


def nested_sum(conjunto) -> int:
    # operacao de Reducao (REDUCE)
    acumulado = 0
    for i in range(len(conjunto)):
        for j in range(len(conjunto[i])):
            acumulado = acumulado + conjunto[i][j]
    return acumulado


if __name__ == '__main__':
    main()
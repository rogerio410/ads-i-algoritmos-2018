def main():
    print('Vetores')

    # vetor = [0, 0, 0, 0, 0]
    # vetor = novo_vetor(4, 'F')
    # vetor2 = novo_vetor(100)
    # nota_x = novo_vetor(5, 10)

    # imprimir_vetor(vetor)
    # imprimir_vetor(vetor2)
    # imprimir_vetor(nota_x)
    # imprimir_vetor_py(nota_x)

    # nota_x = novo_vetor(5)
    # nota_x[0] = 8
    # nota_x[1] = 18
    # nota_x[2] = 95
    # nota_x[3] = 0
    # nota_x[4] = 16
    #
    # imprimir_vetor(nota_x)
    #
    # print(nota_x[1:3])
    # print(bocado(1, 3, nota_x))

    #if contem(o_elemento=20, na_lista=nota_x):
    # if contem(200, nota_x):
    #     print('SIM')
    # else:
    #     print('NÃO')

    letras = novo_vetor(3, 'a')
    letras[1] = 'b'
    letras[2] = 'c'

    imprimir_vetor(letras)
    to_upper(letras)
    imprimir_vetor(bocado(0, 2, letras))


def imprimir_vetor(vetor):
    tam = len(vetor)
    for i in range(tam):
        elemento = vetor[i]
        print('item >', elemento)
    print('Tamanho', tam)


def imprimir_vetor_py(vetor):
    for elemento in vetor:
        print('item >', elemento)


def novo_vetor(tamanho, valor_padrao=None):
    return [valor_padrao] * tamanho


def contem(o_elemento, na_lista) -> bool:
    for i in range(len(na_lista)):
        item_atual = na_lista[i]
        if item_atual == o_elemento:
            return True

    return False


def bocado(inicio, fim, vetor):
    lista_retorno = []

    for posicao in range(len(vetor)):
        item = vetor[posicao]
        if posicao >= inicio and posicao < fim:
            lista_retorno += item,

    return lista_retorno


def to_upper(vetor):
    for i in range(len(vetor)):
        item = vetor[i]
        vetor[i] = chr(ord(item) - 32)


if __name__ == '__main__':
    main()
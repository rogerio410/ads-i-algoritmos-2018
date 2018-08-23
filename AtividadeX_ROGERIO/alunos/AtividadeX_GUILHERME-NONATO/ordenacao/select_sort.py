def swap(lista, a, b):
    aux = lista[a]

    lista[a] = lista[b]
    lista[b] = aux


def eh_maior(a, b):
    return a > b


def eh_menor(a, b):
    return a < b


def select_sort(lista, key=lambda x: x, reverse=False):
    ordem = eh_maior if reverse else eh_menor

    for i in range(len(lista)):
        primeiro_nao_ordenado = i
        a_ser_trocado = i  # O índice do elemento a ser trocado

        for j in range(i+1, len(lista)):
            if ordem(key(lista[j]), key(lista[a_ser_trocado])):
                a_ser_trocado = j

        swap(lista, primeiro_nao_ordenado, a_ser_trocado)
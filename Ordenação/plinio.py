def plinio_sort(lista):
    """Alg. de Plínio Fabrício, 2018.1"""
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        pos_menor = inicio
        pos_maior = inicio

        # procurar posicoes do menor e do maior valores
        for i in range(inicio+1, fim+1):
            if lista[i] < lista[pos_menor]:
                pos_menor = i
            if lista[i] > lista[pos_maior]:
                pos_maior = i

        # fazer a troca: levar menor para o inicio e maior para o fim
        swap(lista, inicio, pos_menor)
        swap(lista, fim, pos_maior)

        # convergir inicio e fim
        inicio += 1
        fim -= 1


def swap(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

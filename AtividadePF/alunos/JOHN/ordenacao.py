def bubble_sort(lista, key=None, reverse=False):
    fim = len(lista)-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(fim):
            a = lista[i]
            b = lista[i + 1]
            if not key:
                if a > b and not reverse or a < b and reverse:
                    swap(lista, i, i+1)
                    swapped = True
            else:
                if key(a) > key(b) and not reverse or key(a) < key(b) and reverse:
                    swap(lista, i, i+1)
                    swapped = True
        fim -= 1
    return lista


def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
from plinio import swap


def bubble_sort(lista, reverse=False, key=None):
    fim = len(lista)-1
    trocou = True
    while trocou:
        trocou = False
        for i in range(fim):
            if not key:
                if (lista[i] > lista[i+1] and not reverse) \
                        or (lista[i] < lista[i+1] and reverse):
                    swap(lista, i, i+1)
                    trocou = True
            else:
                if (key(lista[i]) > key(lista[i+1]) and not reverse) \
                        or (key(lista[i]) < key(lista[i+1]) and reverse):
                    swap(lista, i, i+1)
                    trocou = True

        fim -= 1


def bubble_sort_4_sequences(lista, atributo=None, reverse=False):
    fim = len(lista)-1
    trocou = True
    while trocou:
        trocou = False
        for i in range(fim):
            if (lista[i][atributo] > lista[i+1][atributo] and not reverse) \
                    or (lista[i][atributo] < lista[i+1][atributo] and reverse):
                swap(lista, i, i+1)
                trocou = True

        fim -= 1


def bubble_sort(dados, chave=None, inverso=False):

    trocou = True
    fim = len(dados) - 1

    while trocou:
        trocou = False
        for i in range(fim):
            item_esquerda = dados[i]
            item_direita = dados[i+1]

            esquerda_maior = item_esquerda > item_direita if chave is None else chave(item_esquerda) > chave(item_direita)
            esquerda_menor = item_esquerda < item_direita if chave is None else chave(item_esquerda) < chave(item_direita)

            if (not inverso and esquerda_maior) or (inverso and esquerda_menor):
                trocar(dados, i, item_direita, item_esquerda)
                trocou = True

        fim -= 1


def trocar(dados, i, item_direita, item_esquerda):
    aux = item_esquerda
    dados[i] = item_direita
    dados[i + 1] = aux
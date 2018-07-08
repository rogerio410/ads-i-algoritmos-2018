def main():
    # obtem quantas sublistas
    qtd_sub_listas = int(input('qtd sublista: '))

    # inicializa uma lista vazia no tamanho fornecido
    lista = [0] * qtd_sub_listas

    # recebe cada sublista
    for i in range(qtd_sub_listas):
        entrada = input('SubLista. ex.: x y z: ')
        sublista = entrada.split()

        # converter cada item para int
        for j in range(len(sublista)):
            sublista[j] = int(sublista[j])

        # add sublista à lista
        lista[i] = sublista

    # obter soma dos itens das sublistas
    soma = nested_sum(lista)

    print(lista)
    print('Soma itens: ', soma)


def nested_sum(lista):
    soma = 0
    for i in range(len(lista)):
        sub_lista = lista[i]
        for j in range(len(sub_lista)):
            item_sub_lista = sub_lista[j]
            soma += item_sub_lista
    return soma


if __name__ == '__main__':
    main()
def main():

    lista = [[100, 99], [88, 77]]

    # for i in range(len(lista)):
    #     #     sublista = lista[i]
    #     #     for j in range(len(sublista)):
    #     #         subitem = sublista[j]
    #     #         print(subitem)

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            item = lista[i][j]
            print(item)


if __name__ == '__main__':
    main()
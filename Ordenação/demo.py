from ordenacao import bubble_sort


def main():

    #dados = [4, 3, 1, 7, 2, 0, 6, 5, 10, 8, 9]
    dados = ['Ana', 'Rogerio', 'Maria', 'Luan', 'Frederico', 'Arroz']

    print(dados)
    bubble_sort(dados, inverso=True, chave=lambda x:x[len(x)-1])
    print(dados)



if __name__ == '__main__':
    main()
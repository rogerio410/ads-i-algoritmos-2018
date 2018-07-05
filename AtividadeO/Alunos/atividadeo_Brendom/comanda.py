def main():
    valor_total = 0
    preco = 0
    # trabalho
    while True:
        print("<<<<<<MENU>>>>>>")
        print("Quantidade e C > Cerveja.")
        print("Quantidade e T > Tira Gosto.")
        print("Quantidade e A > Agua.")
        print("0 0 sair:")

        # entrada
        pedido = input("Pedido: ").split()
        quantidade = int(pedido[0])
        produto = pedido[1]
        if quantidade == 0 and produto == '0':
            pagantes = int(input("Quantidade de pagantes: "))
            break
        if produto == "C":
            preco = 8
        if produto == "T":
            preco = 29
        if produto == "A":
            preco = 2
        valor_total += preco * quantidade
    taxa_comicao = (valor_total * 10) / 100
    preco_total = valor_total + taxa_comicao
    preco_por_pagantes = preco_total / pagantes

    # saida
    print("%.2f" % valor_total)
    print("%.2f" % taxa_comicao)
    print("%.2f" % preco_total)
    print("%.2f" % preco_por_pagantes)


if __name__ == '__main__':
    main()

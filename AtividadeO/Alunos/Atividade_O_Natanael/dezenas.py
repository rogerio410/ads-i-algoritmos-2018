# função que verifica se o número possui uma raiz quadrada inteira
def verificar_raiz_quadrada_inteira(numero):
    # variavel que irá conter a raiz(se não possuir uma raiz inteira a variavel terá o valor 0)
    raiz = 1

    # processamento
    while True:
        if raiz * raiz == numero:
            break

        elif raiz * raiz > numero:
            raiz = 0
            break

        raiz += 1

    # retorno(saida)
    return raiz

# função principal
def main():
    # processamento
    for i in range(1000, 10000):
        if ((i // 100) + (i % 100)) == verificar_raiz_quadrada_inteira(i):
            # saida
            print(i)


if __name__ == '__main__':
    main()

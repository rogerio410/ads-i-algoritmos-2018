def main():
    #entrada
    palavra = input('digite a mensagem: ')
    letra_mudada = 0
    pedido_socorro = 'SO'

    #processamento
    for i in range(len(palavra)):
        if palavra[i] == 'S' or palavra[i] == 'O':
            letra_mudada += 0
        else:
            letra_mudada += 1

    #saida
    print(letra_mudada)


if __name__ == '__main__':
    main()
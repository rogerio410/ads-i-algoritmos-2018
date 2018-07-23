def main():

    i = 0
    soma_positivos = 0.0
    qtd_positivos = 0

    while i < 6:
        numero_atual = float(input())
        if numero_atual > 0:
            qtd_positivos = qtd_positivos + 1
            soma_positivos = soma_positivos + numero_atual

        i = i + 1

    media_positivos = soma_positivos / qtd_positivos

    print(qtd_positivos, 'valores positivos')
    print('%.1f' % media_positivos)
    #print('{:.1f}'.format(media_positivos))


if __name__ == '__main__':
    main()
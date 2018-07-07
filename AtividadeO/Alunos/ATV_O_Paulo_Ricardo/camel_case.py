def main():
    frase = input('Digite a frase: ')

    contador_palavras = eh_maiuscula(frase)

    print('Existem {} palavras' .format(contador_palavras))


def eh_maiuscula(frase):
    contador_palavras = 1

    for posicao in range(len(frase) - 1):
        if frase[posicao] == frase[posicao].upper():
            contador_palavras += 1

    return contador_palavras


if __name__ == '__main__':
    main()

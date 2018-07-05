def main():
    frase = input('Frase: ')

    qtd_d_palavras = split_frase(frase)

    print("Qtd Palavras: ", qtd_d_palavras)


def split_frase(frase):
    qtd_maiuscula = 0

    for i in range(len(frase)):
        letra = frase[i]
        if eh_maiuscula(letra):
            qtd_maiuscula += 1

    return qtd_maiuscula + 1


def eh_maiuscula(letra):

    if ord(letra) >= 65 and ord(letra) <= 90:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
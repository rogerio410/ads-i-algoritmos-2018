def main():
    frase = input()

    total = split_frase(frase)

    print(total)


def split_frase(frase):
    total_de_palavras = 1

    for letra in frase: # NAO PERMITIDO
        if eh_maiuscula(letra):
            total_de_palavras += 1

    return total_de_palavras


def eh_maiuscula(caso):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letra in letras:  # NAO PERMITIDO
        if letra == caso:
            return True

    return False


if __name__ == '__main__':
    main()

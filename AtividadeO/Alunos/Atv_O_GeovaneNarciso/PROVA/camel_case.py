def main():
    # entrada
    s = input()

    # saida
    print("Número de palavras na frase:", split_frase(s))


def eh_maiuscula(letra):
    if letra == letra.upper():  # UPPER NAO PERMITIDO
        return True


def split_frase(frase):
    num_palavras = 0
    for i in range(len(frase)):
        if eh_maiuscula(frase[i]):
            num_palavras += 1

    return num_palavras + 1


if __name__ == '__main__':
    main()

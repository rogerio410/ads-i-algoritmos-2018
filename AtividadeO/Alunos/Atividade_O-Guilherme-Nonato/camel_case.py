def main():
    # Entrada
    s = input("Frase em CamelCase: ")
    print()

    # Processamento
    palavras = split_frase(s)

    # Saída
    print(palavras)


def eh_maiuscula(letra):
    return ord(letra) >= 65 and ord(letra) <= 90


def split_frase(frase):
    palavras = 0

    if len(frase) != 0:
        palavras += 1

    for i in range(len(frase)):
        letra = frase[i]

        if eh_maiuscula(letra):
            palavras += 1

    return palavras


if __name__ == "__main__":
    main()

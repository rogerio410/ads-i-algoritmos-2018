def main():
    mensagem = input()
    letras = 'SOS'
    indice = 0
    total = 0

    for letra in mensagem:
        if letra != letras[indice]:
            total += 1

        if indice == len(letras) - 1:
            indice = 0
        else:
            indice += 1

    print(total)


if __name__ == '__main__':
    main()

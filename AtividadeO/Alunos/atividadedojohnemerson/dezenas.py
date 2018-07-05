def main():
    # processamento
    for numero in range(1000, 9999):
        raiz = numero ** (1 / 2)
        primeria_dezena = str(numero)[0] + str(numero)[1]
        segunda_dezena = str(numero)[2] + str(numero)[3]

    # saida
        if int(primeria_dezena) + int(segunda_dezena) == raiz:
            print(numero)


if __name__ == '__main__':
    main()

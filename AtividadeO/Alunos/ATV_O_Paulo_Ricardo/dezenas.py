def main():

    for numero in range(1000, 10000):
        raiz = 0

        # Achando a Raiz
        for possivel_raiz in range(2, 100):
            if possivel_raiz ** 2 == numero:
                raiz = possivel_raiz

        # Criando as dezenas
        numero = str(numero)
        primeira_dezena = int(numero[:2])   # SLICE NAO PERMITIDO
        segunda_dezena = int(numero[-2:])   # SLICE NAO PERMITIDO

        # Conferindo raiz e soma das dezenas
        soma = primeira_dezena + segunda_dezena

        if soma == raiz:
            print(numero)


if __name__ == '__main__':
    main()

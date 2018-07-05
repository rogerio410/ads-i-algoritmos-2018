def raiz_quadrada(n):
    return n**0.5


def divide_milhar(milhar):
    primeira_dezena = milhar // 100
    segunda_dezena = milhar - primeira_dezena*100

    return primeira_dezena, segunda_dezena


def main():
    # Processamento e saída
    for i in range(1000, 10000):
        milhar = i

        primeira_dezena, segunda_dezena = divide_milhar(milhar)

        if primeira_dezena + segunda_dezena == raiz_quadrada(milhar):
            print(milhar)


if __name__ == "__main__":
    main()

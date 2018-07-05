def main():

    for i in range(1000,10000):
        # processamento
        primeira_dezena = i // 100
        segunda_dezena = i - (primeira_dezena * 100)
        raiz = i ** 0.5
        soma = primeira_dezena + segunda_dezena

        if raiz == soma:
            # saida
            print(i)


if __name__ == "__main__":
    main()

def main():
    # trabalho
    for i in range(1000, 10000):
        parte1 = i // 100
        parte2 = i % 100
        raiz = i ** (1 / 2.0)
        soma = parte1 + parte2
        if raiz == soma:

            # saida
            print(i)


if __name__ == '__main__':
    main()

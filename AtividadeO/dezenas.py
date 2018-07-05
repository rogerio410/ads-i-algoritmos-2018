def main():

    for numero in range(1000, 10000):
        dezena1 = numero // 100
        dezena2 = numero % 100

        soma = dezena1 + dezena2

        if numero == soma * soma:
            print(numero, '>', dezena1, ' - ', dezena2)


if __name__ == '__main__':
    main()
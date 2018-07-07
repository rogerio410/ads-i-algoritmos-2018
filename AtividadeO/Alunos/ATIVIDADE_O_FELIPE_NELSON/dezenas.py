def main():

    from math import sqrt  # nao usar!!!

    for numero in range(1000, 10000):
        str_numero = str(numero)
        numero_1 = int(str_numero[0] + str_numero[1])
        numero_2 = int(str_numero[2] + str_numero[3])
        if numero_1 + numero_2 == sqrt(numero):
            print(str_numero)


if __name__ == '__main__':
    main()

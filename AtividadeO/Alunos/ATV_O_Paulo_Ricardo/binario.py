def main():

    numero_binario = input('Digite o numero em binario: ')
    numero_decimal = 0
    potencia = 0

    for i in range(len(numero_binario) - 1, -1, -1):
        numero_decimal += int(numero_binario[i]) * 2**potencia
        potencia += 1

    print(numero_decimal)


if __name__ == '__main__':
    main()

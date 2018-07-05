def main():

    numero_binario = input('Digite um número binário: ')
    numero_decimal = 0

    for numero in range(-1, -len(numero_binario)-1, -1):
        if numero_binario[numero] == '1':
            numero_decimal += 2**(-numero-1)

    print(numero_decimal)


if __name__ == '__main__':
    main()

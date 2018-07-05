def main():
    #entrada
    binario = input('Digite um número binário de 8 digitos: ')
    decimal = 0

    #processamento
    while True:
        if binario[0] == '1':
            decimal += 1 * 128
        if binario[1] == '1':
            decimal += 1 * 64
        if binario[2] == '1':
            decimal += 1 * 32
        if binario[3] == '1':
            decimal += 1 * 16
        if binario[4] == '1':
            decimal += 1 * 8
        if binario[5] == '1':
            decimal += 1 * 4
        if binario[6] == '1':
            decimal += 1 * 2
        if binario[7] == '1':
            decimal += 1 * 1
        break
    #saida

    print(decimal)

if __name__ == '__main__':
    main()

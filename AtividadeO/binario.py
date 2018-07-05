def main():
    binario = input('Bin: ')

    binario = inverter(binario)
    soma = 0

    for i in range(len(binario)):
        bit = binario[i]
        if bit == '1':
            soma = soma + 2 ** i

    print('Dec.: ', soma)


def inverter(texto):
    texto_invertido = ''

    for i in range(len(texto) -1, -1, -1):
        letra = texto[i]
        texto_invertido += letra

    return texto_invertido


if __name__ == '__main__':
    main()
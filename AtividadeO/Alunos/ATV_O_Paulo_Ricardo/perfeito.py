def main():
    numero = int(input('Digite o numero: '))
    resultado = 0

    for verificador in range(1, int(numero / 2) + 1):
        if numero % verificador == 0:
            resultado += verificador

    if resultado == numero:
        print('e perfeito')
    else:
        print('Nao e perfeito')


if __name__ == '__main__':
    main()

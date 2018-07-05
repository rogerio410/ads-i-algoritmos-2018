def main():
    # Entrada
    numero = int(input())

    # Processamento
    perfeito = eh_perfeito(numero)

    if perfeito:
        print('Eh perfeito')
    else:
        print('Nao eh perfeito')


def eh_perfeito(valor):
    resultado = 0

    for numero in range(1, valor):
        if valor % numero == 0:
            resultado += numero

    if resultado == valor:
        return True

    return False


if __name__ == '__main__':
    main()

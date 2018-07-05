# função para saber o tamanho do número
def tamanho_numero(numero):
    tamanho = 0
    aux = 0
    while True:
        aux2 = numero % 10 ** aux
        aux += 1
        if aux2 == numero:
            break
        tamanho += 1
    return tamanho


# função principal
def main():
    # entrada
    numero_binario = int(input('Digite o número na forma binária:'))

    # processamento
    tamanho = tamanho_numero(numero_binario)
    aux = 1
    aux2 = 0
    numero_decimal = 0
    for i in range(tamanho, 0, -1):
        n = (numero_binario % (10 ** aux) // 10 ** aux2)
        if n == 1:
            numero_decimal += 2 ** aux2
        aux += 1
        aux2 += 1

    # saida
    print(numero_decimal)


if __name__ == '__main__':
    main()

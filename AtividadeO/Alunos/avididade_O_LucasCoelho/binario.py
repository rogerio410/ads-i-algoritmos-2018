def main():
    binario = input()

    resultado = binario_para_decimal(binario)

    print(resultado)


def binario_para_decimal(binario):
    posicao = len(binario) - 1
    elevacao = 0
    resultado = 0

    while posicao >= 0:
        resultado += int(binario[posicao]) * potencia(2, elevacao)
        posicao -= 1
        elevacao += 1

    return resultado


def potencia(base, potenciacao):
    if potenciacao == 0:
        return 1

    resultado = base
    aux = base

    for i in range(potenciacao - 1):
        resultado = resultado * aux

    return resultado


if __name__=='__main__':
    main()

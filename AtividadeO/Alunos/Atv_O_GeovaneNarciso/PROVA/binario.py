def main():
    # entrada
    binario = int(input())

    # processamento
    binario = str(binario)[::-1]   # SLICE NAO PERMITIDO
    soma = 0
    for i in range(len(binario)):
        if int(binario[i] != 0):
            soma += int(binario[i]) * 2 ** i

    # saida
    print(soma)


if __name__ == '__main__':
    main()

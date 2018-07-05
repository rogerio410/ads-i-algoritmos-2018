def main():
    # Entrada
    binario = input("Forneça um número natural na base binária: ")

    # Processamento
    decimal = bin2dec(binario)

    # Saída
    print("Equivalente na base decimal:", decimal)


def bin2dec(binario: str):
    decimal = 0

    for i in range(len(binario)-1, -1, -1):
        bit = int(binario[i])
        posicao = len(binario)-i-1

        decimal += bit * 2**posicao

    return decimal


if __name__ == "__main__":
    main()

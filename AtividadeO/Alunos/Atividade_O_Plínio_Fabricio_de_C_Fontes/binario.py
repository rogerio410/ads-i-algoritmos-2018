def main():
    #entrada
    numero_binario = str(input())
    numero_binario = numero_binario[::-1]
    soma = 0

    #processamento
    for indice in range(len(numero_binario)):
        corresponde_em_decimal = (2 ** indice) * int(numero_binario[indice])
        soma += corresponde_em_decimal

    #saida
    print(soma)

if __name__=='__main__':
    main()
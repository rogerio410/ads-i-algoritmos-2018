def main():
    # Apresetação
    print('Esse programa transforma um número binario em decimal.')

    # Entrada
    binario = input('Digite o número em binário: ')

    # Processamento
    soma = 0
    indice = 0
    binario_invertido = binario[::-1]# Inverte o número para que o caculo seja do fim para o começo.

    for i in range(len(binario)):
        passo = int(binario_invertido[indice])
        soma += passo * 2**i
        indice += 1
    # Saída
    print('\nO numero {} binário convertido para decimal é {}.'.format(binario, soma))


if __name__ == '__main__':
    main()

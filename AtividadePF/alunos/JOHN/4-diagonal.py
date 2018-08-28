def main():
    palavra = input('digite a palavra: ')
    matriz = ['-'] * len(palavra)
    contador = 0

    for i in range(len(palavra)):
        matriz[i] = ['-'] * len(palavra)
        matriz[i][contador] = palavra[i]
        contador += 1

    linha = ''
    for j in range(len(matriz)):
        for k in range(len(matriz[j])):
            linha += matriz[j][k]
        linha += '\n'
    print(linha)

if __name__ == '__main__':
    main()

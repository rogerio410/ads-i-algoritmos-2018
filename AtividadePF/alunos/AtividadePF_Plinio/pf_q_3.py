def main():
    nome = input('digite o nome')
    matriz = ['-'] * len(nome)
    inicio = 0
    for i in range(len(matriz)):
        matriz[i] = ['-'] * len(nome)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = nome[inicio]
                inicio +=1
                print(matriz[i])


if __name__=='__main__':
    main()
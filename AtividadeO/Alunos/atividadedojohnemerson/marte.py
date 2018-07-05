def main():
    # entrada
    S = input()

    # processamento
    alterados = 0
    menos_tres_digitos = (S[::-1])[:-3]
    novo_S = menos_tres_digitos[::-1]
    tamanho = len(S)

    while tamanho != 0:
        if S[0] == 'S' and S[1] == 'O' and S[2] == 'S':
            alterados += 0
            S = novo_S
            tamanho -= 3
        else:
            alterados += 1
            S = novo_S
            tamanho -= 3

    # saida
    print(alterados)


if __name__ == '__main__':
    main()

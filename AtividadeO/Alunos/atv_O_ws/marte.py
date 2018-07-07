def main():
    entrada = input('Mensagem recebida da Mars Curiosity:')
    tamanho = len(entrada)
    indice = 0
    erro = 0
    for i in range(tamanho):
        if indice < tamanho:
            for n in range(3):
                letra = entrada[indice]
                if n % 2 == 0:
                    if letra != "S":
                        erro += 1
                else:
                    if letra != "O":
                        erro += 1
                indice += 1
    print('Há {} letras erradas.'.format(erro))


if __name__ == '__main__':
    main()

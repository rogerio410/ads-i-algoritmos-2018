def main():
    mensagem = input()
    erros = 0
    for i in range(0, len(mensagem), 3):
        a = mensagem[i]
        b = mensagem[i + 1]
        c = mensagem[i + 2]

        if a != 'S':
            erros += 1
        if b != 'O':
            erros += 1
        if c != 'S':
            erros += 1

    print('Total de Erros: ', erros)


if __name__ == '__main__':
    main()
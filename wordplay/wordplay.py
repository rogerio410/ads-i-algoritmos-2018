
def main():
    menu = "#### WORD PLAY ####" \
           "\n1 - Palavras N+ carac." \
           "\n2 - Palavras sem 'e'" \
           "\n\n0 - Sair" \
           "\nOpção: "

    while True:
        opcao = int(input(menu))

        if opcao == 0:
            break
        elif opcao == 1:
            palavras_com_mais_de_N_caracteres()


def obter_arquivo():
    arquivo = open('words.txt')
    return arquivo


def palavras_com_mais_de_N_caracteres():
    arquivo = obter_arquivo()
    n = int(input('Limite+? '))
    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) >= n:
            print(palavra)


if __name__ == '__main__':
    main()
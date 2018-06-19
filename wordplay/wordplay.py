def main():
    menu = "\n\n#### WORD PLAY ####" \
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
        elif opcao == 2:
            palavras_sem_e()


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


def palavras_sem_e():
    arquivo = obter_arquivo()
    contar_todas = 0
    contar_sem_e = 0

    for linha in arquivo:
        contar_todas += 1
        palavra = linha.strip()
        if has_no_e(palavra):
            contar_sem_e += 1

    perc = (contar_sem_e / contar_todas) * 100

    print("Palavras sem 'e' = %.2f%%" % perc)


def has_no_e(palavra):
    for i in range(len(palavra)):
        letra = palavra[i]
        if letra == 'e':
            return False
    return True


def avoids(palavra, letras_proibidas):
    """
    :param palavra:
    :param letras_proibidas:
    :return: True se 'palavra' não tiver
            nenhuma das 'letras_proibidas'
    """

    for i in range(len(letras_proibidas)):
        letra_proibida = letras_proibidas[i]
        for j in range(len(palavra)):
            letra = palavra[j]
            if letra_proibida == letra:
                return False

    return True


if __name__ == '__main__':
    main()









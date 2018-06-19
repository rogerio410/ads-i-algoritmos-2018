# Atividade do Cap. 9 do Pense Python


def main():

    menu = '<<<<<<< WORDPLAY >>>>>>> \n\n' \
           '1 - Todas as palavras \n' \
           '2 - Palavras com + de 20 letras \n' \
           '3 - Palavras sem a letra "e" \n' \
           '4 - Palavras sem letras ... \n' \
           '5 - Palavras apenas com letras ... \n' \
           '0 - Sair\n'

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:
            imprimir_palavras()
            # todas
        elif opcao == 2:
            # + de 20 letras
            imprimir_palavras(com_tamanho=20)
            # imprimir_palavras(20)
        elif opcao == 3:
            palavras_has_no_e()
        elif opcao == 4:
            letras = input('Letras proibidas: ')
            palavras_sem_letras(letras)
        elif opcao == 5:
            letras = input('Letras disponíveis: ')
            palavras_apenas_com(letras)
        else:
            print('Opcao inválida!!')

        opcao = int(input(menu))


def palavras_apenas_com(letras):
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()

        if uses_only_apisc(palavra, letras):
            print(palavra)


def imprimir_palavras(com_tamanho: int = 0):
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()

        tamanho_palavra = len(palavra)
        if tamanho_palavra > com_tamanho:
            print(palavra)


def palavras_has_no_e():

    arquivo = open('words.txt')

    total_de_palavras = 0
    total_de_palavras_has_no_e = 0

    for linha in arquivo:
        total_de_palavras += 1
        palavra = linha.strip()

        # if has_no_e(palavra):
        if avoids(palavra, 'e'):
            total_de_palavras_has_no_e += 1
            print(palavra)

    percentual_has_no_e = (total_de_palavras_has_no_e / total_de_palavras) * 100
    print("%.2f%% não têm 'e'" % percentual_has_no_e)


def palavras_sem_letras(letras_proibidas):

    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if avoids(palavra, letras_proibidas):
            print(palavra)


def has_no_e(palavra: str) -> bool:
    nao_tem_e = True
    for letra in palavra:
        if letra == 'e':
            nao_tem_e = False
    return nao_tem_e


def avoids(palavra: str, letras_proibidas: str) -> bool:
    for letra_proibida in letras_proibidas:
        for letra in palavra:
            if letra == letra_proibida:
                return False
    return True


def uses_only(palavra, letras_disponiveis):
    for letra in palavra:
        ocorrencia = 0

        for letra_disponivel in letras_disponiveis:
            if letra == letra_disponivel:
                ocorrencia += 1

        if ocorrencia == 0:
            return False

    return True


def uses_only2(palavra, letras_disponiveis):
    for letra in palavra:
        if letra not in letras_disponiveis:
            return False
    return True


def uses_only_apisc(palavra, letras_disponiveis):
    for i in range(len(palavra)):
        letra = palavra[i]
        ocorrencia = 0

        for j in range(len(letras_disponiveis)):
            letra_disponivel = letras_disponiveis[j]
            if letra == letra_disponivel:
                ocorrencia += 1

        if ocorrencia == 0:
            return False

    return True


if __name__ == '__main__':
    main()

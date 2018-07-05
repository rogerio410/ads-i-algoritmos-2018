# função para ver se a letra é maiuscula
def eh_maiuscula(letra):
    # porcessamento
    if 65 <= ord(letra) <= 90:
        # retorno
        return True
    else:
        # retorno
        return False


# função para verificar o número de palavras em uma frase
def split_frase(frase):
    # contador
    numero_de_palavras = 1

    # processamento
    for i in range(len(frase)):
        if eh_maiuscula(frase[i]):
            numero_de_palavras += 1

    # retorno
    return numero_de_palavras


# função principal
def main():
    # entrada
    s = input('Digite a frase:')

    # saida
    print(split_frase(s))


if __name__ == '__main__':
    main()

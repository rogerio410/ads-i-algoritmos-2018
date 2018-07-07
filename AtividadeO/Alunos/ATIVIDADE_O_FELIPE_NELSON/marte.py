def main():

    mensagem = input('Digite os pedidos de ajuda: ')
    #lista = ['S', 'O', 'S'] # dont use list
    lista = 'SOS' # added
    indice_lista = 0
    letras_alteradas = 0

    for caractere in range(len(mensagem)):
        if mensagem[caractere] != lista[indice_lista]:
            letras_alteradas += 1
        indice_lista += 1
        if indice_lista == 3:
            indice_lista = 0
    
    print(letras_alteradas)


if __name__ == '__main__':
    main()

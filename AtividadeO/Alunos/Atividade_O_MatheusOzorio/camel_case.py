def main():

    #entrada
    frase = ' '
    eh_maiuscula(frase)
    split_frase(frase)

def eh_maiuscula(frase):
    frase = input("Digite a frase: ")
    for i in range (len(frase)):
        if frase[i] == frase[i].upper():
            print("Possui letras maiúsculas.")
            break
        elif frase.islower():
            print("Não possui letras maiúsculas.")
            return

def split_frase(frase):
    contador = 1
    frase = input("Digite a frase para verificar quantas palavras ela possui: ")
    for i in range (len(frase)):
        if frase[i] == frase[i].upper():
            frase[i].split()
            contador +=1
    print("A frase possui %d palavras" %contador)


if __name__ == '__main__':
    main()
def main():
    def eh_maiuscula(caractere_funcao):
        if 65 <= ord(caractere_funcao) <= 90:
            return True

    def split_frase():
        q_palavavras = 1
        frase = input('Digite uma frase em CamelCase: ')
        for caractere in range(len(frase)):
            if eh_maiuscula(frase[caractere]) == True:
                q_palavavras += 1
        print(q_palavavras)
    split_frase()



if __name__ == '__main__':
    main()
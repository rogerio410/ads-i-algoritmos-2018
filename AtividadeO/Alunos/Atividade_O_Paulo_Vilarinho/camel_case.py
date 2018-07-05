def main():
    #entradas
    frase_camel = input("digite a frase em camel case ")
    #processamento
    frase = split_frase(frase_camel)
    #saida
    print(len(frase))


def split_frase(frase_camel):
    nova_frase = ""
    for i in range(len(frase_camel)):
        if eh_maiuscula(frase_camel[i]):
            nova_frase += " " + frase_camel[i]
        else :
            nova_frase += frase_camel[i]
    return nova_frase.split()

def eh_maiuscula(letra):
    if 65 <= ord(letra) <= 90 :
        return True
    else :
        return False

if __name__ == '__main__':
    main()

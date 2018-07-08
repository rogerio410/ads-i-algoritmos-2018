def main():
    entrada = input()
    print(split_frase(entrada))


def eh_maiuscula(letra):
    if 65 <= ord(letra) <= 90:
        maiuscula = True
    else:
        maiuscula = False
    return maiuscula

def split_frase(entrada):
    palavra = 1
    for letra in entrada:
        if eh_maiuscula(letra):
            palavra +=1
    return palavra

if __name__=='__main__':
    main()
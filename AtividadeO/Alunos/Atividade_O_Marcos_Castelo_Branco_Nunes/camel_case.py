def main():
    S = input("Digite a frase em CamelCase: ")

    n_palavras = split_frase(S)
    print(n_palavras)

def split_frase(frase):
    cont = 1
    for i in range(len(frase)):
        if eh_maiuscula(frase[i]):
            cont += 1
    return cont

def eh_maiuscula(letra):
    if 65 <= ord(letra) <= 90:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

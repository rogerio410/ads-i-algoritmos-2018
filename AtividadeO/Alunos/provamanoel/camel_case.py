def main():
    S = input('frase: ')
    split_frase(S)


def eh_maiuscula(letra):
    if ord(letra) <= 90 and ord(letra) >=65:
        return True
    return False



def split_frase(frase):
    conta = 1
    for i in frase:
        if eh_maiuscula(i):
            conta +=1
    print(conta)



if __name__ == '__main__':
    main()


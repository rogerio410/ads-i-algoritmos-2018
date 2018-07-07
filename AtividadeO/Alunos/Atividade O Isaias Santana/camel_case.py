def main():
    maiuscula(input())
    print(split_frase(input()))


def maiuscula(letra):
    if letra == letra.lower():
        print("Caixa baixa")
    elif letra == letra.upper():
        print("Caixa alta")


def split_frase(frase):
    tot_frase = frase.split()
    return len(tot_frase)


if __name__ == '__main__':
    main()
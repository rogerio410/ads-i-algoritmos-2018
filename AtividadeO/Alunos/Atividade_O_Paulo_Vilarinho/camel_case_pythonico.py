def main():
    #entradas
    print(len(split_frase(input("digite a frase em camel case "))))


def split_frase(frase_camel):
    nova_frase = ""
    for i in frase_camel:
        if i.isupper():
            nova_frase += " " + i
        else :
            nova_frase += i
    return nova_frase.split()

if __name__ == '__main__':
    main()

"""
Leia uma frase e mostre cada palavra da frase em uma linha separada.
"""
# Antonio Henrique

def main():
    frase = input()
    palavras = frase.split(' ')

    for palavra in palavras:
        print(palavra)


if __name__ == '__main__':
    main()

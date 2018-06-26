"""
Uma palavra é palíndroma se ela não se altera
quando lida da direita para esquerda.
Por exemplo, raiar é palíndroma.
Escreva um programa que verifique se uma
palavra digitada é palíndroma.
"""


def main():
    palavra = input()
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print("Palindroma")
    else:
        print("Nao e palindroma")


if __name__ == '__main__':
    main()
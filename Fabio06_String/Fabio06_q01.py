"""
Faça a criptografia de uma frase digitada pelo usuário.
Na criptografia, a frase deverá ser invertida e as
 consoantes deverão ser substituídas pelo caractere
"""
# Resolvido por Guilherme Nonato + Natanael


def main():
    texto = input()

    texto_invertido = ''
    vogais = 'aeiou '

    for i in range(len(texto)-1, -1, -1):
        caractere = texto[i]
        if caractere.lower() not in vogais:
            caractere = '#'
        texto_invertido += caractere
    print(texto_invertido)


if __name__ == '__main__':
    main()

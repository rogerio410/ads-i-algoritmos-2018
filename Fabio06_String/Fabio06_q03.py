"""
Leia uma frase e gere uma nova frase,
retirando os espaços entre as palavras.
"""
# Francimara e Heverton

def main():
    frase = input()

    nova_frase = ''
    palavras = frase.split()

    for palavra in palavras:
        nova_frase += palavra

    print(nova_frase)


if __name__ == '__main__':
    main()

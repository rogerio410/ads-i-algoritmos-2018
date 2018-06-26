import random

def main():
    arquivo = open('alunos.txt')
    linhas = arquivo.readlines()

    random.shuffle(linhas)

    contador = 0
    while contador < len(linhas):
        sorteado = linhas.pop()
        print('Sorteado: ', sorteado)
        contador = contador + 1
        input()

if __name__ == '__main__':
    main()
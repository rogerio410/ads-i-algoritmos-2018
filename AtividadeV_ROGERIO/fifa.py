from importacao import *
from funcionalides import *
import os


def main():
    # importar o arquivo
    jogos = importar()

    menu = '***** FIFA 1930 -- 2014 *****\n' \
           '1 - Quantidade de Jogos\n' \
           '0 - Sair\n'

    opcao = int(input(menu))

    # loop do Menu de opcões
    while opcao != 0:
        if opcao == 1:
            total_jogos(jogos)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

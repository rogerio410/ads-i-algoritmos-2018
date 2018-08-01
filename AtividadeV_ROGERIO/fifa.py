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

    while True:
        if opcao == 1:
            total_jogos(jogos)
        elif opcao == 0:
            break
        else:
            print('Opcao Invalida!')

        # pedir nova opcao
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

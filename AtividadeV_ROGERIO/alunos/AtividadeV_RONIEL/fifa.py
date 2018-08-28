from importacao import *
from funcionalides import *
import os


def main():
    # importar o arquivo
    jogos = importar()
    matriz_dados = importar_matriz(jogos)

    os.system("cls")
    menu = '***** FIFA 1930 -- 2014 *****\n' \
           '1 - Quantidade de Jogos\n' \
           '2 - Listar todos os jogos de uma seleção\n' \
           '3 - Listar todos os jogos por parte do nome\n' \
           '4 - Listar todos os jogos de final\n' \
           '0 - Sair\n'

    opcao = int(input(menu))

    # loop do Menu de opcões
    while opcao != 0:
        if opcao == 1:
            total_jogos(jogos)
        elif opcao == 2:
            jogos_selecao_especifica(matriz_dados)
        elif opcao == 3:
            jogos_por_parte_nome(matriz_dados)
        elif opcao == 4:
            jogos_de_final(matriz_dados)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('cls')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

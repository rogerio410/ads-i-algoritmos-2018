from importacao_alunos import *
from funcionalidades import *
from ordenacao import *


def main():

    # listas vazias
    alunos = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(alunos)


    # opcoes FAKE, demonstracao apenas
    menu = '***** ALUNOS PROF. R1 *****\n' \
           '1 - Total de Alunos\n' \
           '2 - Listar Alunos\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = int(input(menu))
    while opcao != 0:

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(alunos)
        elif opcao == 2:
            lista_todos(alunos)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

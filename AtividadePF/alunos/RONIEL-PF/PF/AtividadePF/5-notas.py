from importacao_alunos import *
from funcionalidades import *
from ordenacao import *


def main():

    # listas vazias
    alunos = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(alunos)
    alunos = converte_notas_para_float(alunos)
    alunos = add_media(alunos)
    alunos = add_situacao(alunos)

    ''' VERIFICAR ARQUIVO
    for i in range(len(alunos)):
        print(alunos[i])'''


    # opcoes FAKE, demonstracao apenas
    menu = '***** ALUNOS PROF. R1 *****\n' \
           '1 - Total de Alunos\n' \
           '2 - Listar Alunos\n' \
           '3 - Imprimir tabela\n' \
           '4 - Estatisticas da turma\n' \
           '5 - Buscar aluno por parte do nome\n' \
           '6 - Buscar por faixa de nota\n' \
           '7 - Buscar por situacao\n' \
           '8 - Media de nota da turma por alunos condicao(A)\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = int(input(menu))
    while opcao != 0:

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(alunos)
        elif opcao == 2:
            lista_todos(alunos)
        elif opcao == 3:
            imprimir_tabela(alunos)
        elif opcao == 4:
            estatistica_turma(alunos)
        elif opcao == 5:
            aluno_por_parte_do_nome(alunos)
        elif opcao == 6:
            por_faixa_de_nota(alunos)
        elif opcao == 7:
            por_situacao(alunos)
        elif opcao == 8:
            media_alunos_por_A(alunos)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('cls')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

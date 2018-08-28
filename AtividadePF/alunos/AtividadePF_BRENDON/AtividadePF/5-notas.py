from importacao_alunos import *
from funcionalidades import *
from ordenacao import *


def main():
    # listas vazias
    alunos = []
    alunos_dicionario = []
    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(alunos)

    for i in range(len(alunos)):
        aluno = alunos[i]
        nome = aluno[0]
        estado = aluno[1]
        nota1 = aluno[2]
        nota2 = aluno[3]
        aluno = {'nome': nome, 'estado': estado, 'nota1': nota1, 'nota2': nota2, 'media': 0, 'situacao': 0}
        alunos_dicionario.append(aluno)

    media(alunos_dicionario)
    # opcoes FAKE, demonstracao apenas
    menu = '***** ALUNOS PROF. R1 *****\n' \
           '1 - Total de Alunos\n' \
           '2 - Listar Alunos\n' \
           '3 - listar o resultado: \n' \
           '4 - Exibe a estatistica da turma:\n' \
           '5 - Procura aluno por parte do nome:\n' \
           '7 - Exibe a media de nota dos alunos A:\n' \
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
            exibe_alunos(alunos_dicionario)
        elif opcao == 4:
            lista_estatistica(alunos_dicionario)
        elif opcao == 5:
            buscar_por_parte(alunos_dicionario)
        elif opcao == 7:
            media_alunos_a(alunos_dicionario)



        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

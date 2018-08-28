from importacao_alunos import *
from funcionalidades import *
from ordenacao import *


def main():

    # listas vazias
    alunos = []

    # preencher listas com dados importados: lista de dicionarios
    todos_os_alunos = importar()
    for i in range(len(todos_os_alunos)):
        aluno = {'nome': todos_os_alunos[i][0], 'situacao': todos_os_alunos[i][1], 'nota_parte_1': float(todos_os_alunos[i][2]),
                 'nota_parte_2': float(todos_os_alunos[i][3]), 'bonus': 0, 'media': 0, 'situacao_2': 0}
        alunos.append(aluno)


    for j in range(len(alunos)):
        if alunos[j]['situacao'] == 'A':
            alunos[j]['bonus'] += 0.5

        media_ponderada = ((alunos[j]['nota_parte_1'] * 1) + (alunos[j]['nota_parte_2'] * 2)) / (1 + 2)
        alunos[j]['media'] = media_ponderada + (alunos[j]['bonus'])

        if alunos[j]['media'] >= 7.0:
            alunos[j]['situacao_2'] = 'APROVADO'
        elif alunos[j]['media'] >= 4.0:
            alunos[j]['situacao_2'] = 'PROVA FINAL'
        else:
            alunos[j]['situacao_2'] = 'REPROVADO'


    menu = '***** ALUNOS PROF. R1 *****\n' \
           '1 - Total de Alunos\n' \
           '2 - Listar Alunos\n' \
           '3 - Resultados\n' \
           '4 - Estatística da Turma\n' \
           '5 - Tabela Ordenável\n' \
           '6 - Busca de Aluno\n' \
           '7 - Filtrar por faixa de nota\n' \
           '8 - Listar por situação\n' \
           '9 - Média de Nota da turma considerando apenas alunos A\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = int(input(menu))
    while opcao != 0:

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(todos_os_alunos)
        elif opcao == 2:
            lista_todos(alunos)
        elif opcao == 3:
            resultado(alunos)
        elif opcao == 4:
            estatisticas(alunos)
        elif opcao == 5:
            tabela_ordenavel(alunos)
        elif opcao == 6:
            buscar_alunos_por_parte_do_nome(alunos)
        elif opcao == 7:
            filtrar_por_faixa_de_nota(alunos)
        elif opcao == 8:
            listar_por_situacao(alunos)
        elif opcao == 9:
            print('Média da turma = {:.1f}'.format(media_de_notas(alunos)))
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

from importacao_alunos import *
from funcionalidades import *


def main():
    alunos = []

    # Funcionalidades iniciais
    inicializar_dados(alunos)
    alunos_total = len(alunos)
    formatacao_dos_nomes(alunos)
    situacoes = [
        {'situacao': 'APROVADO', 'quantidade': 0, 'porcentagem': 0},
        {'situacao': 'PROVA FINAL', 'quantidade': 0, 'porcentagem': 0},
        {'situacao': 'REPROVADO', 'quantidade': 0, 'porcentagem': 0},
        {'situacao': 'EVADIDO', 'quantidade': 0, 'porcentagem': 0}]

    resumo_com_contagem(alunos, situacoes, alunos_total)

    menu = '***** ALUNOS PROF. R1 *****\n' \
           '1 - Resultado\n' \
           '2 - Estatistica da turma\n' \
           '3 - Tabela Ordenável\n' \
           '4 - Busca de Aluno\n' \
           '5 - Por faixa de nota\n' \
           '6 - Média de Nota da turma\n' \
           '0 - Sair\n'

    opcao = int(input(menu))
    while opcao != 0:
        if opcao == 1:
            lista_todos(alunos)
        elif opcao == 2:
            lista_todos(situacoes)
        elif opcao == 3:
            lista_todos(ordenar_tabela_por_escolha(alunos))
        elif opcao == 4:
            lista_todos(buscar_por_parte_do_nome(alunos))
        elif opcao == 5:
            lista_todos(busca_faixa_de_nota(alunos))
        elif opcao == 6:
            print('A media da turma foi de %.2f' % media_da_turma(alunos))
        else:
            print('Opcao Invalida!')

        input('Enter para continuar...')
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

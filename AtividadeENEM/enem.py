from importacao import importar, tratar_dados
from enem_utils import *


def main():
    # importar o arquivo
    escolas = importar()

    # tratar os dados
    tratar_dados(escolas)

    # gerar nota_geral de cada escola
    calcular_nota_geral(escolas)

    qtd_escolas = len(escolas)
    print('Escolas importadas: {}'.format(qtd_escolas))

    menu = '1 - Top N Brasil\n' \
           '2 - Top N EScolas por UF\n' \
           '3 - Ranking Estados\n' \
           '4 - Top N Escolas por Area' \
           '0 - Sair\n'

    while True:

        opcao = int(input(menu))

        if opcao == 1:
            top_n_escolas(escolas)
        if opcao == 2:
            top_n_escolas_por_uf(escolas)
        if opcao == 3:
            ranking_uf(escolas)
        if opcao == 4:
            top_n_escolas_por_competencia(escolas)
        elif opcao == 0:
            break
        else:
            print('Opcao Invalida!')



if __name__ == '__main__':
    main()
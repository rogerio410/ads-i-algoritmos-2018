from importacao import importa_coligacao, importa_vereador
from Atividade_X_II import *
import os

def main():

    coligacoes = ()
    vereadores = ()

    menu = '***** Eleições Teresina/2012 *****\n' \
           '1 - Total de Coligações\n' \
           '2 - Listar Coligações\n' \
           '0 - Sair\n'

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            total(coligacoes)
        elif opcao == 2:
            lista_todos(coligacoes)
        else:
            print('Opcao Invalida')


def inicializa_dados(coligacoes, vereadores):
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes')
    dados_vreadores = importar_vereadores('dados/candidatos_e_votos')

    print(f'{len(dados_coligacoes)}')
    print(f'{len(dados_vereadores)}')


        input('Enter para continuar...')
        os.system('cls')


if __name__=='__main__':
    main()
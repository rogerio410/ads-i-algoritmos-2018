from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    coligacoes = importar_coligacoes('partidos_coligacoes_the_2012.csv')
    vereadores = importar_vereadores('candidatos_e_votos_vereador_THE_2012.csv')

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total de votos validos\n' \
           '4 - Quociente Eleitoral\n' \
           '5 - Total de votos por coligacao\n' \
           '6 - Total de vagas por (Quociente Partidario)\n' \
           '7 - Vagas de sobra(vagas por media)\n' \
           '8 - Imprimir lista de vereadores(por Regra de Eleicao Proporcional e mais votados primeiro)\n' \
           '9 - Imprimir lista de vereadores(mais votados primeiro)\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = -1
    while opcao != 0:

        # pedir nova opcao
        opcao = int(input(menu))

        # variaveis e atualizacoes.
        add_votos_por_coligacao(coligacoes)
        QE = quociente_eleitoral(total_de_votos_validos(vereadores), 29)
        add_vagas_e_sobras(coligacoes, QE)

        # verificar opcao e invocar funcao responsável

        if opcao == 1:
            total(coligacoes)
        elif opcao == 2:
            lista_todos(coligacoes)
        elif opcao == 3:
            print('Total de votos validos =', total_de_votos_validos(vereadores))
        elif opcao == 4:
            print('Quociente eleitoral =', QE)
        elif opcao == 5:
            imprimir_votos_por_coligacao(coligacoes)
        elif opcao == 6:
            total_de_vagas(coligacoes)
        elif opcao == 9:
            imprimir_vereadores_mais_votados(vereadores)
        elif opcao == 0:
            break
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

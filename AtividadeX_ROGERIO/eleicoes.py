from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total Votos Válidos\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = -1
    while opcao != 0:

        # pedir nova opcao
        opcao = int(input(menu))

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(coligacoes)
        elif opcao == 2:
            lista_todos(coligacoes)
        elif opcao == 3:
            total_votos_validos(vereadores)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # Coligações
    for item in dados_coligacoes:
        coligacao = {}
        coligacao['coligacao'] = item
        coligacao['total_votos'] = 0
        coligacao['qtd_vagas'] = 0
        coligacao['votos_sobra_total'] = 0
        coligacoes.append(coligacao)

    # Vereadores
    for item in dados_vereadores:
        vereador = {}
        vereador['nome'] = item[0]
        vereador['numero'] = int(item[1])
        vereador['partido'] = item[2]
        vereador['coligacao'] = item[3]
        vereador['total_votos'] = int(item[4])
        vereadores.append(vereador)


    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

from importacao import *
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    inicializar_dados(coligacoes, vereadores)

    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
            '1 - Total de Votos Válidos\n' \
            '2 - Quociente Eleitoral\n' \
            '3 - Total de votos por coligação\n' \
            '4 - Total de vagas por Quociente Partidário\n' \
            '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = -1
    while opcao != 0:

        # pedir nova opcao
        opcao = int(input(menu))

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total_votos(vereadores)
        elif opcao == 2:
            quociente_eleitoral(vereadores)
        elif opcao == 3:
            lista = total_votos_coligacoes(coligacoes, vereadores)
        elif opcao == 4: #Chamar o total de votos por coligações primeiro.
            total_vagas_partidario(coligacoes)
        elif opcao == 5:
            show_afonso(coligacoes)

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
    for item in dados_coligacoes:
        coligacao = {}
        coligacao["coligacao"] = item
        coligacao["total_votos"] = 0
        coligacao["qtd_vagas"] = 0
        coligacao["votos_sobra_total"] = 0
        coligacoes.append(coligacao)


    for item in dados_vereadores:
        vereador = {}
        vereador['nome'] = item[0]
        vereador['numero'] = item[1]
        vereador['partido'] = item[2]
        vereador['coligacao'] = item[3]
        vereador['total_votos'] = int(item[4])
        vereadores.append(vereador)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()
from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)
    
    ordenar_por(vereadores, "total_votos", reverse=True)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total de votos válidos\n' \
           '4 - Quociente eleitoral\n' \
           '5 - Total de votos por coligação\n' \
           '6 - Total de vagas por QP\n' \
           '7 - Eleitos em votação não proporcional\n' \
           '8 - Percentual de cada partido\n' \
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
            listar_coligacoes(coligacoes)

        elif opcao == 3:
            total_votos_validos(vereadores)

        elif opcao == 4:
            quociente_eleitoral(vereadores)

        elif opcao == 5:
            total_votos_coligacao(coligacoes, vereadores)
            exibir_coligacoes(coligacoes)

        elif opcao == 6:
            vagas_por_qp(coligacoes, vereadores)

        elif opcao == 7:
            eleitos_nao_proporcional(vereadores)

        elif opcao == 8:
            percentual_partidos(vereadores)

        elif opcao == 0:
            break

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
    for item in dados_coligacoes:
        coligacao = {"coligacao": item, "total_votos": 0, "qtd_vagas": 0, "votos_sobra_total": 0}
        coligacoes.append(coligacao)

    for item in dados_vereadores:
        candidato = {"nome": item[0], "numero": item[1], "partido": item[2], "coligacao": item[3], "total_votos": int(item[4])}
        vereadores.append(candidato)

    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)
    printa_coligacoes(coligacoes)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Votos Válidos\n' \
           '2 - Quociente Eleitoral\n' \
           '3 - Total de Votos por Coligação\n' \
           '4 - Total de Vagas por Quociente Partidário\n' \
           '5 - Vagas de sobra\n' \
           '7 - Vereadores por voto geral\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = -1
    while opcao != 0:

        # pedir nova opcao
        opcao = int(input(menu))

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            print("Total de votos válidos: ", total_votos_validos(vereadores))
        elif opcao == 2:
            print("Quociente Eleitoral: ", quociente_eleitoral(vereadores))
        elif opcao == 3:
            print("Votos por Coligação: ",
                  printa_coligacoes(ordenados_por(total_votos_coligacao(vereadores, coligacoes),
                                                  "total_votos", inverso=True)))
        elif opcao == 4:
            print("Total de Vagas por Quociente Partidário: ",
                  printa_coligacoes(ordenados_por(total_vagas_qp(vereadores, coligacoes), "total_votos", inverso=True)))
        elif opcao == 5:
            print("Vagas de sobra: ", vagas_sobra(coligacoes))
        elif opcao == 7:
            print("Vereadores por votos geral: ",
                  printa_vereadores(ordenados_por(vereadores, "total_votos", inverso=True)))
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    for item in dados_coligacoes:
        coligacao = {"coligacao": item, "total_votos": 0, "qtd_vagas": 0, "votos_sobra_total": 0}
        coligacoes.append(coligacao)

    for item in dados_vereadores:
        vereador = {"nome": item[0], "numero": int(item[1]), "partido": item[2], "coligacao": item[3],
                    "total_votos": int(item[4])}
        vereadores.append(vereador)

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()


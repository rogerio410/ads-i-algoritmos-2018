from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():
    vereadores, coligacoes = inicializar_dados()
    ordenar_dicionario(vereadores)

    # Dados auxiliares
    vagas = 29
    votos_validos = total_de_votos_validos(vereadores)
    quociente = quociente_eleitoral(votos_validos, vagas)
    total_de_votos_coligacao(vereadores, coligacoes)
    ordenar_dicionario(coligacoes)
    resto_das_vagas = total_de_vagas_por_coligacao(coligacoes, quociente, vagas)

    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de votos validos\n' \
           '2 - Quociente eleitoral\n' \
           '3 - Total votos por coligacao\n' \
           '4 - total de vagas por (Quociente Partidario)\n' \
           '5 - Vagas de sobra (Vagas por media)\n' \
           '6 - ' \
           '0 - Sair \n' \
           '>>> '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print('%d votos válidos\n' % votos_validos)
        elif opcao == 2:
            print('Queciente eleitoral(QE): %d\n' % quociente)
        elif opcao == 3:
            lista_todos(coligacoes)
            print('Coligacoes com total de votos\n')
        elif opcao == 4:
            lista_todos(coligacoes)
            print('Coligacoes com total de votos, e vagas')
            print('Restaram %d vagas\n' % resto_das_vagas)
        elif opcao == 5:
            pass
        else:
            print('Opcao Invalida!')

        input('Enter para continuar...')
        opcao = int(input(menu))


        '''
        # limpar a tela
        os.system('clear')  # se Windows: 'cls'
        '''


def inicializar_dados():

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    dados_vereadores, dados_coligacoes = formatar_dados(dados_vereadores, dados_coligacoes)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'

    return dados_vereadores, dados_coligacoes


def formatar_dados(vereadores, coligacoes):
    coligacao = []
    vereador = []

    for v in vereadores:
        vereador.append({'nome': v[0], 'numero': v[1], 'partido': v[2], 'coligacao': v[3], 'total_votos': int(v[4])})

    for c in coligacoes:
        coligacao.append({'coligacao': c, 'total_votos': 0, 'qtd_vagas': 0, 'votos_sobra_total': 0})

    return vereador, coligacao


if __name__ == '__main__':
    main()

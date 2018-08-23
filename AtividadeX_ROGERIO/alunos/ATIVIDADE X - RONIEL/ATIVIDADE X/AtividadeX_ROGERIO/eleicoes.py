from importacao import *
from funcionalidades import *
import os

def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    coligacoes, vereadores = inicializar_dados(coligacoes, vereadores)

    vereadores = transforma_inteiro(vereadores)
    coligacoes = add_total_votos_cada_coligacao(coligacoes, vereadores)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total de votos válidos\n' \
           '4 - Quociente_eleitoral\n' \
           '5 - Total de votos por coligação\n' \
           '9 - Vereadores eleitos caso eleição não proporcional\n' \
           '11 - Percentual de votos de cada partido\n' \
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
            votos_validos(vereadores)
        elif opcao == 4:
            quociente_eleitoral(vereadores)
        elif opcao == 5:
            total_votos_por_coligacao(coligacoes)
        elif opcao == 9:
            lista_eleitos_eleicao_nao_proporcional(vereadores)
        elif opcao == 11:
            percentual_votos_cada_partido(vereadores)
        else:
            if opcao == 0:
                break
            
            print('Opcao Invalida!')


        # limpar a tela
        input('Enter para continuar...')
        os.system('cls')  # se Windows: 'cls'

  
def inicializar_dados(coligacoes, vereadores):
    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('cls')  # ou 'cls'

    return dados_coligacoes, dados_vereadores



if __name__ == '__main__':
    main()

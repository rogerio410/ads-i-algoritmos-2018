from importacao import *
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    coligacoes, vereadores = inicializar_dados(coligacoes, vereadores)
    

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Consulta 01: Total de votos válidos\n' \
           '4 - Consulta 02: Quociente Eleitoral\n' \
           '5 - Consulta 03: Total Votos por coligacão\n' \
           '6 - Consulta 04: Total de vagas por (coeficiente Partidario)\n' \
           '7 - Consulta 05: Vagas de Sobra (Vagas por média)\n' \
           '8 - Consulta 06: Imprimir lista dos vereadores eleitos\n' \
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
            print('Total de votos válidos:', somatorio_atributo(coligacoes,'total_votos'))
        elif opcao == 4:
            coeficiente = coeficiente_eleitoral(coligacoes)
            print('Quociente Eleitoral: %.0f' %coeficiente)
        elif opcao == 5:
            total_votos_coligacao(coligacoes, 'total_votos')
        elif opcao == 6:
            total_vagas(coligacoes)
        elif opcao == 7:
            print('feito junto com a consulta 04')
        elif opcao == 8:
            imprimir_lista_vereadores_aprovador(coligacoes, vereadores)            
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('cls')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    total_votos(dados_coligacoes, dados_vereadores)
    
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

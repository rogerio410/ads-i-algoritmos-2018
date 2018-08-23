from importacao import *
from funcionalidades import *


def main():

    # preencher listas com dados importados: lista de dicionarios
    coligacoes, candidatos = inicializar_dados()

    # opcoes FAKE, demonstracao apenas

    menu = "*---------------------------***** ELEIÇÕES TERESINA/2012 *****----------------------------------*" \
           "\n| 1 - Total de Votos válidos                                                                    |" \
           "\n| 2 - Quociente Eleitoral                                                                       |" \
           "\n| 3 - Total de Votos por Coligação                                                              |" \
           "\n| 4 - Total de Vagas por Quociente Partidário e os Votos de Sobra                               |" \
           "\n| 5 - Cálculo para Vagas Restantes                                                              |" \
           "\n| 6 - Imprimir lista dos Vereadores(nome, nome do partido, total de votos)                      |" \
           "\n| 0 -                                                                                           |" \
           "\n Digite a opção: "


    # Loop do Menu de opcões
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            print(cabecalho('Total de Votos Válidos'))
            print('Somatório de votos válidos:', total_votos(candidatos))

        elif opcao == 2:
            print(cabecalho('Quociente Eleitoral'))
            print('Quociente:', quociente_eleitoral(candidatos))

        elif opcao == 3:
            total_votos_por_coligacao(candidatos, coligacoes)
            print(cabecalho('Coligações e Total de Votos'))
            imprimir_coligacoes_e_total_voltos(coligacoes)

        elif opcao == 4:
            quantidade_de_vagas(candidatos, coligacoes)
            quantidade_de_sobras(candidatos, coligacoes)
            print(cabecalho('Quantidade de Vagas e Quantidade de Sobras de cada Coligação'))
            imprimir_coligacoes_qtd_vagas_qtd_sobras(coligacoes)

        elif opcao == 5:
            vagas_de_sobra_final(candidatos, coligacoes)
            imprimir_vagas(coligacoes)

        elif opcao == 6:
            imprimir_vereadores_eleitos(candidatos, coligacoes)

        else:
            print('\nOpcao Invalida!')

        input('\nAperte ENTER para continuar...\n')
        opcao = int(input(menu))

def inicializar_dados():

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')

    return dados_coligacoes, dados_vereadores


if __name__ == '__main__':
    main()

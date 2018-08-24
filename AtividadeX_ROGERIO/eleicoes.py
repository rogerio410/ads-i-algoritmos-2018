from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # Variaveis gerais
    coligacoes = []
    vereadores = []
    vereadores_eleitos = []
    total_votos = 0
    quociente_eleitoral = 0
    qtd_vagas = 29
    qtd_vagas_sobra = 0

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)

    # Computacoes iniciais
    total_votos = total_votos_validos(vereadores)
    quociente_eleitoral = total_votos // qtd_vagas

    # Distribuir Vagas
    qtd_vagas_sobra = calcular_qtd_vagas_por_quociente_eleitoral(coligacoes, qtd_vagas, quociente_eleitoral)
    calcular_qtd_vagas_por_media(coligacoes, qtd_vagas_sobra)

    # Marcar eleitos e filtrá-los
    marca_vereadores_eleitos(coligacoes, vereadores)
    vereadores_eleitos = filtrar_conjunto(vereadores, 'eleito', True)

    # Ordenar eleitos e coligacoes por Votos
    bubble_sort(vereadores_eleitos, chave=lambda x: x['total_votos'], inverso=True)
    bubble_sort(coligacoes, chave=lambda x:x['qtd_vagas'], inverso=True)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total Votos Válidos\n' \
           '4 - Quociente Eleitoral\n' \
           '6 - Vereadores eleitos\n' \
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
            print('Total Votos = {}'.format(total_votos))
        elif opcao == 4:
            print('Quociente Eleitoral = {:.2f}'.format(quociente_eleitoral))
        elif opcao == 6:
            lista_todos(vereadores_eleitos)
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
    # Vereadores
    for item in dados_vereadores:
        vereador = {}
        vereador['nome'] = item[0]
        vereador['numero'] = int(item[1])
        vereador['partido'] = item[2]
        vereador['coligacao'] = item[3]
        vereador['total_votos'] = int(item[4])
        vereador['eleito'] = False
        vereadores.append(vereador)

    # Coligações
    for item in dados_coligacoes:
        coligacao = {}
        coligacao['coligacao'] = item
        vereadores_coligacao = filtrar_conjunto(vereadores, 'coligacao', coligacao['coligacao'])
        coligacao['total_votos'] = reduzir_conjunto(vereadores_coligacao, 'total_votos')
        coligacao['qtd_vagas'] = 0
        coligacao['votos_sobra_total'] = 0
        coligacoes.append(coligacao)


    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

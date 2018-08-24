from importacao import *
from funcionalidades import *
import os


def main():

    # Variaveis gerais
    coligacoes = []
    vereadores = []
    qtd_vagas = 29

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

    # Ordenar eleitos e coligacoes por total de votos
    bubble_sort(vereadores_eleitos, chave=lambda x: x['total_votos'], inverso=True)
    bubble_sort(coligacoes, chave=lambda x:x['qtd_vagas'], inverso=True)

    # Menu
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total Votos Válidos\n' \
           '4 - Quociente Eleitoral\n' \
           '6 - Vereadores Eleitos\n' \
           '0 - Sair\n'

    opcao = int(input(menu))
    while opcao != 0:

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

        # limpar a tela e pedir nova opcao
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'
        opcao = int(input(menu))


if __name__ == '__main__':
    main()

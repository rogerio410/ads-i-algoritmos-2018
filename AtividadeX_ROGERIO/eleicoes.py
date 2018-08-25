from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []
    CADEIRAS = 29

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)

    # Dados iniciais
    votos_validos = reduzir_por_atributo_e_operacao(vereadores, 'total_votos', '+')
    quociente_eleitoral = votos_validos // CADEIRAS

    # calcular Vagas por QP
    vagas_distribuidas = calcular_vagas_por_QP(coligacoes, quociente_eleitoral)
    vagas_sobrantes = CADEIRAS - vagas_distribuidas
    print('Vagas a distribuir por media = {}'.format(vagas_sobrantes))

    # calcular vagas por MEDIA
    calcular_vagas_por_media(coligacoes, vagas_sobrantes)

    # marcar os eleitos
    marcar_os_eleitos_para_cada_coligacao(coligacoes, vereadores)
    eleitos = filtrar_por_atributo(vereadores, 'eleito', True)
    bubble_sort(vereadores, chave=lambda x: x['total_votos'], inverso=True)
    eleitos_nao_proporcionais = vereadores[:CADEIRAS]

    # ordenar coligacao e eleitos por total de vagas
    bubble_sort(coligacoes, chave=lambda x:x['qtd_vagas'], inverso=True)
    bubble_sort(eleitos, chave=lambda x:x['total_votos'], inverso=True)


    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total de Votos\n' \
           '4 - Quociente Eleitoral\n' \
           '5 - Eleitos\n' \
           '6 - Eleitos Não-Proporcional\n' \
           '0 - Sair\n'

    # Loop do Menu de opcões
    opcao = int(input(menu))
    while opcao != 0:

        # verificar opcao e invocar funcao responsável
        if opcao == 1:
            total(coligacoes)
        elif opcao == 2:
            lista_todos(coligacoes)
        elif opcao == 3:
            print('Votos Válidos = {}'.format(votos_validos))
        elif opcao == 4:
            print('Quociente = {}'.format(quociente_eleitoral))
        elif opcao == 5:
            lista_todos(eleitos)
        elif opcao == 6:
            lista_todos(eleitos_nao_proporcionais)
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'

        # pedir nova opcao
        opcao = int(input(menu))


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
        vereador['numero'] = item[1]
        vereador['partido'] = item[2]
        vereador['coligacao'] = item[3]
        vereador['total_votos'] = int(item[4])
        vereador['eleito'] = False
        vereadores.append(vereador)

    # Coligacoes
    for item in dados_coligacoes:
        coligacao = {}
        coligacao['coligacao'] = item
        vereadores_coligacao = filtrar_por_atributo(vereadores, 'coligacao', coligacao['coligacao'])
        coligacao['total_votos'] = reduzir_por_atributo_e_operacao(vereadores_coligacao, 'total_votos', '+')
        coligacao['qtd_vagas'] = 0
        coligacao['media'] = 0.0
        coligacoes.append(coligacao)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

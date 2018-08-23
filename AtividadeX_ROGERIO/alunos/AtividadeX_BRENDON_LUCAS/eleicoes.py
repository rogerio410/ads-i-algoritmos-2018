from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []

    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)

    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - votos validos\n' \
           '4 - Quociente eleitor\n' \
           '5 - total de votos das coligaçoes\n' \
           '6 - total de vagas\n' \
           '9 - eleitos sem o modelo proporcional\n' \
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
            total_votos_coligacao(vereadores, coligacoes)
        elif opcao == 6:
            total_de_vagas(coligacoes, vereadores)
        elif opcao == 9:
            vereadores_eleitos(vereadores)
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
    # TODO
    for i in range(len(dados_vereadores)):
        nome = dados_vereadores[i][0]
        numero= dados_vereadores[i][1]
        partido = dados_vereadores[i][2]
        coligacao=dados_vereadores[i][3]
        total_votos=dados_vereadores[i][4]
        candidato = {'nome': nome, 'numero': numero, 'partido': partido, 'coligacao': coligacao,'total_votos': total_votos}
        vereadores.append(candidato)

    for j in range(len(dados_coligacoes)):
        coligacao = dados_coligacoes[j]
        total_votos = 0
        qtd_vagas = 0
        votos_sobra_total = 0
        coligacao = {'coligacao':coligacao,'total_votos':total_votos,'qtd_vagas':qtd_vagas,'votos_sobra_total':votos_sobra_total}
        coligacoes.append(coligacao)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'

    return coligacoes, vereadores
if __name__ == '__main__':
    main()

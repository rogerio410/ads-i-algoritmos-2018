from importacao import *
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
           '3 - Listar Vereadores\n'\
           '4 - Total de Votos Válidos\n'\
           '5 - Para o Quociente Eleitoral \n'\
           '6 - Para o Total de Votos por Coligação\n'\
           '7 - Para total de Vagas por Quociente Eleitoral de cada coligação \n'\
           '8 - Para calculo de vagas de Sobra\n'\
           '9 - lista dos que seriam eleitos se o sistema fosse voto direto\n'\
           '0 - Sair'

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
            lista_todos(vereadores)
        elif opcao == 4:
            print(total_votos(vereadores))
        elif opcao == 5:
            total = total_votos(vereadores)
            coeficiente = total_votos(vereadores) // 29
            print(coeficiente)
        elif opcao == 6:
            total_votos_por_coligacao(vereadores, coligacoes)
            print(coligacoes)

        elif opcao == 7:
            total_votos_por_coligacao(vereadores, coligacoes)
            coeficiente = total_votos(vereadores) // 29
            for i in range(len(coligacoes)):
                coligacoes[i]['total_vagas'] = coligacoes[i]['qtd_votos'] // coeficiente

            print(coligacoes)
            sobra = 29
            for i in range(len(coligacoes)):
                sobra -= coligacoes[i]['total_vagas']
            print('sobraram {} vagas'.format(sobra))

        elif opcao == 8:
            total_votos_por_coligacao(vereadores, coligacoes)
            coeficiente = total_votos(vereadores) // 29
            for i in range(len(coligacoes)):
                coligacoes[i]['total_vagas'] = coligacoes[i]['qtd_votos'] // coeficiente
            sobra = 29
            for i in range(len(coligacoes)):
                sobra -= coligacoes[i]['total_vagas']
            while sobra > 0:
                for i in range(coligacoes):
                    coligacoes[i]

        elif opcao == 9:
           print(ordem_votacao(vereadores))

        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('cls')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')

    for item in dados_coligacoes:
        coligacao = {"coligacao": item, "qtd_votos": 0, "total_vagas": 0, "votos_sobra_total": 0}
        coligacoes.append(coligacao)

    for item in range(543):
        vereador = {'nome': dados_vereadores[item][0], 'numero': dados_vereadores[item][1], 'nome_partido':dados_vereadores[item][2], 'coligacao': dados_vereadores[item][3], 'total_votos': dados_vereadores[item][4]}
        vereadores.append(vereador)
    # Log

    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))


    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

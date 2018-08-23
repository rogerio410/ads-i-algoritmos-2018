from importacao import *
from funcionalidades import *
import os


def main():

    # listas vazias
    coligacoes = []
    vereadores = []
    coligacoes_preenchidas = []
    partidos = []
    # preencher listas com dados importados: lista de dicionarios
    inicializar_dados(coligacoes, vereadores)
    total_de_votos_por_coligacao(coligacoes,vereadores)
    total_de_vagas_por_quociente(coligacoes)
    partidos = gerar_partidos(vereadores)
    total_de_votos_por_coligacao(partidos,vereadores)
    # opcoes FAKE, demonstracao apenas
    menu = '***** ELEIÇÕES TERESINA/2012 *****\n' \
           '1 - Total de Coligacoes\n' \
           '2 - Listar Coligacoes\n' \
           '3 - Total de Votos\n' \
           '4 - Quociente Eleitoral\n' \
           '5 - Total de votos por coligacao\n' \
           '6 - Total de Vagas por coligacao\n' \
           '7 - Total de Vagas por coligacao após o preenchimento\n' \
           '8 - Vereadores Eleitos\n' \
           '9 - Vereadores que seriam Eleitos caso o sistema nao fosse proporcional\n' \
           '10 - Lista de n suplentes\n' \
           '11 - Percentual de votos dos partidos\n' \
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
            total_de_votos(vereadores)
        elif opcao == 4:
            quociente_eleitoral(vereadores,29)
        elif opcao == 5:
            lista_todos(coligacoes,so_votos)
        elif opcao == 6:
            lista_todos(coligacoes,so_vagas)
            vagas_sobraram(coligacoes)
        elif opcao == 7:
            coligacoes_preenchidas = preencher_vagas(coligacoes)
            lista_todos(coligacoes_preenchidas,so_vagas)
        elif opcao == 8:
            eleitos = vereadores_eleitos(coligacoes_preenchidas, vereadores)
            lista_todos(eleitos)
            print(len(eleitos))
        elif opcao == 9:
            eleitos_nao_proporcional = vereadores_mais_votados(vereadores)
            lista_todos(eleitos_nao_proporcional)
        elif opcao == 10:
            n = int(input("Quantos suplentes por coligacao"))
            suplentes = vereadores_suplentes(coligacoes,vereadores,n)
            lista_todos(suplentes)
        elif opcao == 11:
            lista_todos(partidos,key=so_porcentagem)


        else:
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
    for dados in dados_coligacoes :
        coligacao = {"coligacao":dados,"total_votos":0,"qtd_vagas":0,'votos_sobra_total':0}
        coligacoes.append(coligacao)
    for dados in dados_vereadores:
        vereador = {"nome":dados[0],"numero":dados[1],"partido":dados[2],"coligacao":dados[3],"total_votos":dados[4]}
        vereadores.append(vereador)
    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

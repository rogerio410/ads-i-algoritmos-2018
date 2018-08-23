from importacao import importar_coligacoes, importar_vereadores
from funcionalidades import total, lista_todos, total_de_votos, quociente_eleitoral, voto_por_coligacao, atualizar_qtd_vagas
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
           '3 - Total de Votos\n' \
           '4 - Quociente eleitoral\n' \
           '5 - Total de Votos por Coligacao\n' \
           '6 - Total de Vagas coligacao\n' \
           '0 - Sair\n' 
           

    # Loop do Menu de opcões
    opcao = -1
    colig =atualizar_qtd_vagas(coligacoes, vereadores)
    dic = voto_por_coligacao(coligacoes, vereadores)
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
            quociente = quociente_eleitoral(vereadores)
            print("Quociente eleitoral igual a %d votos"%quociente)
        elif opcao == 5:
            
            for item in dic:
                print(item['coligacao'], 'Votos -', item['total_votos'])
        elif opcao == 6:
            for c in colig:
                print(c['coligacao'], 'Vagas por Coligacao -', c['qtd_vagas'])
        elif opcao == 0:
            return 0
        else:
            print('Opcao Invalida!')

        # limpar a tela
        input('Enter para continuar...')
        os.system('clear')  # se Windows: 'cls'


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv') 

    # povoando a lista de coligacoes com os dicionarios para pcada ajoasdja.,jdaos
    for item in dados_coligacoes:
        coligacao = {"coligacao": item, "total_votos": 0, "qtd_vagas": 0, "votos_sobra_total": 0}
        coligacoes.append(coligacao)

    # povoar vereadores

    for item in dados_vereadores:
        vereador = {"nome": item[0], "numero": item[1], "partido": item[2], "coligacao": item[3], "total_votos": item[4]}
        vereadores.append(vereador)

    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Organizar dados de acordo com o solicitado
    # TODO

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'


if __name__ == '__main__':
    main()

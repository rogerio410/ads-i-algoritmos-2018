"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""
from funcionalidades import filtrar_conjunto, reduzir_conjunto
import os


def importar_coligacoes(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip())

    return registros


def importar_vereadores(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip().split(';'))

    return registros


def inicializar_dados(coligacoes, vereadores):

    # Importar dados
    dados_coligacoes = importar_coligacoes('dados/partidos_coligacoes_the_2012.csv')
    dados_vereadores = importar_vereadores('dados/candidatos_e_votos_vereador_THE_2012.csv')


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


    # Log
    print('Carregados {} coligacoes e {} vereadores'.format(len(dados_coligacoes), len(dados_vereadores)))

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'
"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""
import os


def importar(arquivo):
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip().split(';'))

    return registros


def inicializar_dados(alunos):

    # Importar dados
    dados_alunos = importar('alunos.txt')

    # Log
    print('Carregados {} alunos'.format(len(dados_alunos)))

    for a in dados_alunos:
        alunos.append(a)

    # Limpar a tela
    input('Enter para ir ao Menu...')
    os.system('clear')  # ou 'cls'
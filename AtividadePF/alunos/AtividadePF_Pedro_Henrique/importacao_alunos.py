"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""
# import os
from funcionalidades import verifica_situacao


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

    situacao = lambda x: 'ATIVO' if x == 'A' else 'EVADIDO'
    media = lambda x, y, situacao: ((x * 1 + y * 2) / 3) + 0.5 if situacao == 'ATIVO' else ((x * 1 + y * 2) / 3)

    for aluno in dados_alunos:
        dicio = {}
        dicio['nome'] = aluno[0]
        dicio['situacao'] = situacao(aluno[1])
        dicio['nota_um'] = float(aluno[2])
        dicio['nota_dois'] = float(aluno[3])
        dicio['media'] = media(dicio['nota_um'], dicio['nota_dois'], dicio['situacao'])
        dicio['resultado'] = verifica_situacao(dicio['media'])
        alunos.append(dicio)

    input('Enter para ir ao Menu...')
    # Limpar a tela
    # os.system('clear')  # ou 'cls'

"""
    Funções relacionadas a importação de dados e eventuais tratamentos e conversões.
"""


def importar(arquivo='Partidas_CopaMundo_1930_2014.csv'):
    """
    https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte

    Depois, Pref > File Encoding > "Add file e select" ISO-8859-1

    """
    fin = open(arquivo, encoding="ISO-8859-1")

    jogos = []
    fin.readline()  # titulos das colunas
    for linha in fin.readlines():
        jogos.append(linha)

    return jogos

def importar_matriz(jogos):

    matriz = []
    for linha in jogos:
        linha_limpa = linha.strip()
        dados_matriz = linha_limpa.split(';')
        matriz.append(dados_matriz)

    return matriz

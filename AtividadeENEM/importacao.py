def importar(arquivo='enem2014_nota_por_escola.csv'):
    """
    https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte

    Depois, Pref > File Encoding > "Add file e select" ISO-8859-1

    """
    fin = open(arquivo, encoding="ISO-8859-1")

    escolas = []
    for linha in fin.readlines():
        linha_limpa = linha.strip()
        dados_escola = linha_limpa.split(';')
        escolas.append(dados_escola[1:])

    return escolas


def tratar_dados(escolas):

    for i in range(len(escolas)):
        for j in range(len(escolas[i])):
            # se eh para transformar para float
            if j >= 6 and j <= 11:
                escolas[i][j] = float(escolas[i][j].replace(',', '.'))













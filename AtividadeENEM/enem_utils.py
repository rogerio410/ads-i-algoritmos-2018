

def calcular_nota_geral(escolas):

    for i in range(len(escolas)):
        media_geral = (escolas[i][6] + escolas[i][11]) / 2
        escolas[i].append(media_geral)


def top_n_escolas(escolas):

    # TODO: e se nao nao digitar um int.
    n = int(input('Quantas escolas? '))

    # ordenar por nota_geral
    escolas_ordenadas_geral = sorted(escolas, key=por_nota_geral, reverse=True)

    # escrever n escolas
    exibir_escolas(n, escolas_ordenadas_geral)


def por_nota_geral(escola):
    return escola[12]


def exibir_escolas(n, escolas, coluna=12):
    for i in range(n):
        exibir_escola(i, escolas[i], coluna)


def exibir_escola(pos, escola, coluna):
    # colunas 0, 1, 2, 12
    print(pos+1, escola[0], escola[1], escola[2], '{:.1f}'.format(escola[coluna]))


def filtrar_escolas_por_estado(escolas, uf):

    escolas_filtradas = []
    for i in range(len(escolas)):
        if escolas[i][2] == uf:
            escolas_filtradas.append(escolas[i])
    return escolas_filtradas


def top_n_escolas_por_uf(escolas):
    # pedir os dados (N e UF)
    n = int(input('Quantas escolas? '))
    uf = input('Sigla do Estado? ')

    # filtrar as escolas pela UF
    escolas_uf = filtrar_escolas_por_estado(escolas, uf)

    # ordenar pela nota_geral
    escolas_uf = sorted(escolas_uf, key=por_nota_geral, reverse=True)

    # escrever n escolas
    exibir_escolas(n, escolas_uf)


def ranking_uf(escolas):

    ufs = obter_siglas_estados(escolas)
    ufs.sort()

    media_estadual = []

    for i in range(len(ufs)):
        uf = ufs[i]
        somatorio_uf = 0.0
        cont_uf = 0
        for j in range(len(escolas)):
            if escolas[j][2] == uf:
                somatorio_uf += escolas[j][12]
                cont_uf += 1

        media_uf = somatorio_uf / cont_uf
        media_estadual.append([uf, media_uf])

    media_estadual.sort(key=lambda registro: registro[1], reverse=True)

    # imprimir medias dos estados
    for i in range(len(media_estadual)):
        print(i+1, '\t', media_estadual[i][0], '\t', media_estadual[i][1])


def obter_siglas_estados(escolas):

    estados = []
    for i in range(len(escolas)):
        uf = escolas[i][2]
        achou = False
        for j in range(len(estados)):
            if uf == estados[j]:
                achou = True
                break
        if achou == False:
            estados.append(uf)

    return estados

def top_n_escolas_por_competencia(escolas):

    menu = '1 - Linguagens\n' \
           '2 - Matemática\n' \
           '3 - Ciências da Natureza\n' \
           '4 - Ciências Humanas\n' \
           '5 - Redação\n\n' \
           'Digite a opcao: '

    opcao = int(input(menu))

    while opcao < 1 or opcao > 5:
        opcao = int(input(menu))

    hab = 5 + opcao

    n = int(input('Quantas escolas? '))

    # ordenar por nota_geral
    escolas_ordenadas_especificas = sorted(escolas, key=lambda x:x[hab], reverse=True)

    # escrever n escolas
    exibir_escolas(n, escolas_ordenadas_especificas, hab)



















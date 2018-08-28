from ordenacao import bubble_sort


# ##### FUNCIONALIDADES MENU #####


def total(dados):
    print(cabecalho('Total de Alunos'), "Alunos: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)


def formatacao_dos_nomes(alunos):
    for aluno in alunos:
        nome = aluno['nome'].split()
        nome = ('%s %s' % (nome[0], nome[len(nome) - 1]))
        aluno['nome'] = nome


def resumo_com_contagem(alunos, situacoes, total_de_alunos):
    for situacao in situacoes:
        dados_situacao = filtrar_por_atributo(alunos, 'resultado', situacao['situacao'])
        situacao['quantidade'] = len(dados_situacao)
        situacao['porcentagem'] = (len(dados_situacao) / total_de_alunos) * 100

    evadidos = reduzir_informacao(alunos, 'situacao', 'somatorio', 'EVADIDO')

    situacoes[2]['quantidade'] = situacoes[2]['quantidade'] - evadidos
    situacoes[2]['porcentagem'] = (situacoes[2]['quantidade'] / total_de_alunos) * 100
    situacoes[3]['quantidade'] = evadidos
    situacoes[3]['porcentagem'] = (evadidos / total_de_alunos) * 100


def ordenar_tabela_por_escolha(alunos):
    ordem = int(input('Ordenar por:\n'
                      '1 - Nome\n'
                      '2 - Nota\n'
                      '3 - Situaçao\n'
                      '>>> '))

    reverse = int(input('\nOrdem:\n'
                        '1 - Crescente\n'
                        '2 - Decrescente\n>>> '))

    numero_de_alunos = int(input('Quantos alunos deseja exibir: '))

    if ordem == 1:
        ordem = 'nome'
    elif ordem == 2:
        ordem = 'media'
    else:
        ordem = 'situacao'

    if reverse == 1:
        reverse = False
    else:
        reverse = True

    bubble_sort(alunos, chave=lambda x: x[ordem], inverso=reverse)
    resultado = []
    for i in range(numero_de_alunos):
        resultado.append(alunos[i])

    return resultado


def buscar_por_parte_do_nome(alunos):
    nome = input('Digite o nome ou parte dele: ')
    nome = nome.upper()
    return filtrar_por_atributo(alunos, 'nome', nome, like=True)


def busca_faixa_de_nota(alunos):
    inicio = float(input('Digite a nota inicial: '))
    fim = float(input('Digite o limite: '))

    return filtrar_por_faixa(alunos, inicio, fim)


def media_da_turma(alunos):
    alunos_ativos = filtrar_por_atributo(alunos, 'situacao', 'ATIVO')
    somatorio_das_notas = reduzir_informacao(alunos_ativos, 'media', 'adicao')
    return somatorio_das_notas / len(alunos_ativos)


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ALUNOS PROF. R1 *****\n'
            ' >> {} <<\n'.format(titulo))


def reduzir_informacao(lista, atributo, acao, busca=None):
    resultado = 0
    for item in lista:
        if acao == 'adicao' and not busca:
            resultado += item[atributo]
        elif acao == 'somatorio' and item[atributo] == busca:
            resultado += 1
    return resultado


def filtrar_por_faixa(lista, a, b):
    resultado = []
    for item in lista:
        media = item['media']
        if a <= media <= b:
            resultado.append(item)
    return resultado


def filtrar_por_atributo(lista, atributo, valor=None, like=False):
    resultado = []
    for item in lista:
        if not valor:
            if not tem_na_lista(resultado, atributo, item[atributo]):
                resultado.append(item)
        else:
            if item[atributo] == valor and not like:
                resultado.append(item)
            elif valor in item[atributo] and like:
                resultado.append(item)
    return resultado


def tem_na_lista(lista, atributo, valor):
    for item in lista:
        if item[atributo] == valor:
            return True
    return False


def verifica_situacao(nota):
    if nota >= 7:
        return 'APROVADO'
    elif nota >= 4:
        return 'PROVA FINAL'
    else:
        return 'REPROVADO'

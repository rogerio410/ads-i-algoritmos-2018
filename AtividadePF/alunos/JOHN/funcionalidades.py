# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ALUNOS PROF. R1 *****\n'
            ' >> {} <<\n'.format(titulo))


def mape(funcao, lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(funcao(lista))
    return nova_lista


from ordenacao import *
# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Alunos'), "Alunos: {}".format(len(dados)))


def lista_todos(alunos):
    for i in range(len(bubble_sort(alunos, key=lambda x: x['nome']))):
        print('Nome:', alunos[i]['nome'])

def resultado(alunos):
    for i in range(len(alunos)):
        print('Nome(nome e último sobrenome):', alunos[i]['nome'].split()[0], alunos[i]['nome'].split()[-1])
        print('Notas:', alunos[i]['nota_parte_1'], 'e', alunos[i]['nota_parte_2'])
        print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
        print('Situação:', alunos[i]['situacao_2'])
        print()

def estatisticas(alunos):
    total_alunos = 0
    total_evadidos = 0
    total_aprovados = 0
    total_reprovados = 0
    total_prova_final = 0
    for i in range(len(alunos)):
        aluno = alunos[i]
        total_alunos += 1
        if aluno['situacao'] == 'E':
            total_evadidos += 1
        if aluno['situacao_2'] == 'APROVADO':
            total_aprovados += 1
        if aluno['situacao_2'] == 'REPROVADO':
            total_reprovados += 1
        if aluno['situacao_2'] == 'PROVA FINAL':
            total_prova_final += 1
    print('Total de alunos =', total_alunos)
    print('Total de alunos evadidos =', total_evadidos)
    print('Percentual de alunos evadidos = {:.1f}%'.format((total_evadidos*100)/total_alunos))
    print('Total de alunos aprovados =', total_aprovados)
    print('Percentual de alunos aprovados = {:.1f}%'.format((total_aprovados * 100) / total_alunos))
    print('Total de alunos reprovados =', total_reprovados)
    print('Percentual de alunos reprovados = {:.1f}%'.format((total_reprovados * 100) / total_alunos))
    print('Total de alunos em prova final =', total_prova_final)
    print('Percentual de alunos em prova final = {:.1f}%'.format((total_prova_final * 100) / total_alunos))

def tabela_ordenavel(alunos):
    criterio = int(input('Digite o critério de ordenação(1-nome, 2-nota(média), 3-situação): '))
    ordem = int(input('Digite a ordem de preferência(1-crescente, 2-decrescente): '))
    quantidade = int(input('Digite a quantidade de alunos que deseja exibir: '))

    if criterio == 1:
        if ordem == 1:
            resultado(bubble_sort(alunos, key=lambda x: x['nome'])[:quantidade])
        elif ordem == 2:
            resultado(bubble_sort(alunos, key=lambda x: x['nome'], reverse=True)[:quantidade])
    elif criterio == 2:
        if ordem == 1:
            resultado(bubble_sort(alunos, key=lambda x: x['media'])[:quantidade])
        elif ordem == 2:
            resultado(bubble_sort(alunos, key=lambda x: x['media'], reverse=True)[:quantidade])
    elif criterio == 3:
        opcao = int(input('1-Aprovados, 2-Reprovados, 3-Prova final, 4-Evadidos'))
        if opcao == 1:
            if ordem == 1:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'APROVADO')[:quantidade])
            elif ordem == 2:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'APROVADO', reverse=True)[:quantidade])
        elif opcao == 2:
            if ordem == 1:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'REPROVADO')[:quantidade])
            elif ordem == 2:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'REPROVADO', reverse=True)[:quantidade])
        elif opcao == 3:
            if ordem == 1:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'PROVA FINAL')[:quantidade])
            elif ordem == 2:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'PROVA FINAL', reverse=True)[:quantidade])
        elif opcao == 4:
            if ordem == 1:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'EVADIDO')[:quantidade])
            elif ordem == 2:
                resultado(bubble_sort(alunos, key=lambda x: x['situacao_2'] == 'EVADIDO', reverse=True)[:quantidade])


def buscar_alunos_por_parte_do_nome(alunos):
    nome = input('Digite a parte do nome: ')
    nome = nome.upper()
    for i in range(len(alunos)):
        if nome in alunos[i]['nome']:
            print('Nome:', alunos[i]['nome'])
            print('Notas:', alunos[i]['nota_parte_1'], 'e', alunos[i]['nota_parte_2'])
            print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
            print('Situação:', alunos[i]['situacao_2'])
            print()


def filtrar_por_faixa_de_nota(alunos):
    faixa_1 = int(input('Digite o primeiro número da faixa: '))
    faixa_2 = int(input('Digite o segundo número da faixa: '))
    faixa = [faixa_1, faixa_2]
    print('\nFaixa de {} à {}:\n'.format(faixa[0], faixa[1]))

    for i in range(len(alunos)):
        if faixa[0] <= alunos[i]['media'] <= faixa[1]:
            print('Nome:', alunos[i]['nome'])
            print('Notas:', alunos[i]['nota_parte_1'], 'e', alunos[i]['nota_parte_2'])
            print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
            print('Situação:', alunos[i]['situacao_2'])
            print()


def listar_por_situacao(alunos):
    situacao = int(input('Digite a situação desejada(1-Aprovados, 2-Reprovados, 3-De prova final, 4-Evadidos): '))

    if situacao == 1:
        for i in range(len(alunos)):
            if alunos[i]['situacao_2'] == 'APROVADO':
                print('Nome:', alunos[i]['nome'])
                print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
                print('Situação:', alunos[i]['situacao_2'])
                print()
    elif situacao == 2:
        for i in range(len(alunos)):
            if alunos[i]['situacao_2'] == 'REPROVADO':
                print('Nome:', alunos[i]['nome'])
                print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
                print('Situação:', alunos[i]['situacao_2'])
                print()
    elif situacao == 3:
        for i in range(len(alunos)):
            if alunos[i]['situacao_2'] == 'PROVA FINAL':
                print('Nome:', alunos[i]['nome'])
                print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
                print('Situação:', alunos[i]['situacao_2'])
                print()
    elif situacao == 4:
        for i in range(len(alunos)):
            if alunos[i]['situacao'] == 'E':
                print('Nome:', alunos[i]['nome'])
                print('Média Calculada: {:.1f}'.format(alunos[i]['media']))
                print('Situação:', alunos[i]['situacao_2'])
                print()


def media_de_notas(alunos):
    soma = 0
    total = 0
    for i in range(len(alunos)):
        if alunos[i]['situacao'] == 'A':
            total += 1
            soma += alunos[i]['media']
    return soma/total
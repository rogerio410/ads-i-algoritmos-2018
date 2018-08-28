from ordenacao import bubble_sort


# ##### FUNCIONALIDADES MENU #####


def total(dados):
    print(cabecalho('Total de Alunos'), "Alunos: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)


def media(alunos):
    situacao = ''
    for i in range(len(alunos)):
        nota1_aluno = float(alunos[i]['nota1'])
        nota2_aluno = float(alunos[i]['nota2'])

        if alunos[i]['estado'] == 'A':
            bonos = 0.5
        else:
            bonos = 0
        media_aluno = ((nota1_aluno * 1 + nota2_aluno * 2) / 3) + bonos
        alunos[i]['media'] = media_aluno
        if media_aluno >= 7:
            situacao = 'APROVADO'
        if 7 > media_aluno >= 4:
            situacao = 'PROVA FINAL'
        if media_aluno < 4:
            situacao = 'REPROVADO'
        if alunos[i]['estado'] == 'E':
            situacao = 'EVADIDO'
        alunos[i]['situacao'] = situacao


def exibe_alunos(alunos):
    for i in range(len(alunos)):
        mostra_aluno(alunos[i])


def media_alunos_a(alunos):
    soma_media = 0
    cont = 1
    for i in range(len(alunos)):
        aluno = alunos[i]
        estado_aluno = aluno['estado']
        if estado_aluno == 'A':
            soma_media += (float(aluno['nota1']) + float(aluno['nota2'])) / 2
            cont += 1
    media_alunos = soma_media / cont
    print('Media de alunos A: %.1f' % media_alunos)


def buscar_por_parte(alunos):
    parte = input('Digite a parte do nome ate 4 caracteres: ')
    if len(parte) == 1:
        for i in range(len(alunos)):
            nome_aluno = alunos[i]['nome']
            for j in range(len(nome_aluno)):
                if parte == nome_aluno[j]:
                    mostra_alunos_2(alunos[i])
    elif len(parte) == 3:
        for i in range(len(alunos)):
            nome_aluno = alunos[i]['nome']
            for j in range(len(nome_aluno) - 1):
                if parte == nome_aluno[j - 1] + nome_aluno[j] + nome_aluno[j + 1]:
                    mostra_alunos_2(alunos[i])
    elif len(parte) == 2:
        for i in range(len(alunos)):
            nome_aluno = alunos[i]['nome']
            for j in range(len(nome_aluno)):
                if parte == nome_aluno[j - 1] + nome_aluno[j]:
                    mostra_alunos_2(alunos[i])
    elif len(parte) == 4:
        for i in range(len(alunos)):
            nome_aluno = alunos[i]['nome']
            for j in range(len(nome_aluno) - 2):
                if parte == nome_aluno[j - 1] + nome_aluno[j] + nome_aluno[j + 1] + nome_aluno[j + 2]:
                    mostra_alunos_2(alunos[i])
    else:
        print('Não encontrado.')


def lista_estatistica(alunos):
    cont_aprovado = 0
    cont_reprovado = 0
    cont_prova_final = 0
    cont_evadido = 0
    cont_alunos = 0
    for i in range(len(alunos)):
        aluno = alunos[i]
        cont_alunos += 1
        if aluno['situacao'] == 'APROVADO':
            cont_aprovado += 1
        if aluno['situacao'] == 'REPROVADO':
            cont_reprovado += 1
        if aluno['situacao'] == 'PROVA FINAL':
            cont_prova_final += 1
        if aluno['situacao'] == 'EVADIDO':
            cont_evadido += 1
    porcentagem_aprovados = (cont_aprovado * 100) / cont_alunos
    porcentagem_reprovados = (cont_reprovado * 100) / cont_alunos
    porcentagem_prova_final = (cont_prova_final * 100) / cont_alunos
    porcentagem_evadidos = (cont_evadido * 100) / cont_alunos

    print("aprovados:", cont_aprovado, 'alunos', 'percentual de %.2f %%' % porcentagem_aprovados)
    print('Reprovados:', cont_reprovado, 'alunos', 'percentual de %.2f %%' % porcentagem_reprovados)
    print('Prova final:', cont_prova_final, 'alunos', 'percentual de %.2f %%' % porcentagem_prova_final)
    print('Evadidos:', cont_evadido, 'alunos', 'percentual de %.2f %%' % porcentagem_evadidos)


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ALUNOS PROF. R1 *****\n'
            ' >> {} <<\n'.format(titulo))


def mostra_aluno(aluno):
    for i in range(1):
        nome = aluno['nome'].split()
        print(nome[0], nome[len(nome) - 1], 'nota 1 =', aluno['nota1'], 'nota 2 =', aluno['nota2'], 'media = %.2f' %
              aluno['media'], aluno['situacao'])


def mostra_alunos_2(aluno):
    for i in range(1):
        print(aluno['nome'], 'nota 1 =', aluno['nota1'], 'nota 2 =', aluno['nota2'], 'media = %.2f' %
              aluno['media'], aluno['situacao'])
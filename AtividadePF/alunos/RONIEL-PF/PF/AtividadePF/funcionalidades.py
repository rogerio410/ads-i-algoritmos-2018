from ordenacao import bubble_sort
# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Alunos'), "Alunos: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)

def imprimir_tabela(alunos):
	print("*** IMPRIMIR TABELA ***")
	for i in range(len(alunos)):
		print('-'*120)
		print("Nome: %s..... Nota1: %.1f..... Nota2: %.1f..... Media:: %.1f...... Situacao: %s" % (alunos[i][0], alunos[i][2], alunos[i][3], alunos[i][4], alunos[i][5]))
		print('-'*120)


def estatistica_turma(alunos):
	ap = 0
	pf = 0
	re = 0
	ev = 0
	for i in range(len(alunos)):
		if(alunos[i][5] == 'APROVADO'):
			ap = ap+1
		elif(alunos[i][5] == 'PROVA FINAL'):
			pf = pf+1
		elif(alunos[i][5] == 'REPROVADO'):
			re = re+1
		elif(alunos[i][5] == 'EVADIDO'):
			ev = ev+1

	print("*** ESTATISTICAS DA TURMA ***")
	print(ap, "aprovados")
	print(pf, "em prova final")
	print(re, "reprovados")
	print(ev, "evadidos")


def aluno_por_parte_do_nome(alunos):
	print("*** ALUNO POR PARTE DO NOME ***")
	nome = (input("Digite: "))

	for i in range(len(alunos)):
		if(nome.upper() in alunos[i][0].upper()):
			print('-'*120)
			print("Nome: %s..... Nota1: %.1f..... Nota2: %.1f..... Media:: %.1f...... Situacao: %s" % (alunos[i][0], alunos[i][2], alunos[i][3], alunos[i][4], alunos[i][5]))
	print('-'*120)


def por_faixa_de_nota(alunos):
	print("*** BUSCAR POR FAIXA DE NOTA ***")
	a, b = input("Informe a faixa (separar por espaço): ").split(' ')
	a = float(a)
	b = float(b)

	for i in range(len(alunos)):
		if(alunos[i][4] >=a and alunos[i][4] <=b):
			print('-'*120)
			print("Nome: %s..... Media:: %.1f" % (alunos[i][0], alunos[i][4]))
	print('-'*120)


def por_situacao(alunos):
	print("*** LISTAR POR SITUACAO ***")
	situacao = input("Qual a situacao? digite igualmente (APROVADO, PROVA FINAL, REPROVADO, EVADIDO)\n>> ")

	for i in range(len(alunos)):
		if(alunos[i][5] == situacao):
			print('-'*120)
			print("Nome: %s..... Media:: %.1f..... Situacao: %s" % (alunos[i][0], alunos[i][4], alunos[i][5]))
		elif(alunos[i][5] == situacao):
			print('-'*120)
			print("Nome: %s..... Media:: %.1f..... Situacao: %s" % (alunos[i][0], alunos[i][4], alunos[i][5]))
		elif(alunos[i][5] == situacao):
			print('-'*120)
			print("Nome: %s..... Media:: %.1f..... Situacao: %s" % (alunos[i][0], alunos[i][4], alunos[i][5]))
		elif(alunos[i][5] == situacao):
			print('-'*120)
			print("Nome: %s..... Media:: %.1f..... Situacao: %s" % (alunos[i][0], alunos[i][4], alunos[i][5]))
	print('-'*120)


def media_alunos_por_A(alunos):
	print("*** MEDIA ALUNOS POR CONDICAO(A) ***")

	media = 0
	cont = 0
	for i in range(len(alunos)):
		if(alunos[i][1] == 'A'):
			media = media + alunos[i][4]
			cont = cont+1
	media = media / cont

	print("Media = %.1f" % media)



# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ALUNOS PROF. R1 *****\n'
            ' >> {} <<\n'.format(titulo))

def converte_notas_para_float(alunos):
	for i in range(len(alunos)):
		alunos[i][2] = float(alunos[i][2])
		alunos[i][3] = float(alunos[i][3])

	return alunos

def add_media(alunos):
	for i in range(len(alunos)):
		if(alunos[i][1] == 'A'):
			media = ((alunos[i][2]*1 + alunos[i][3]*2) / (1+2)) + 0.5

			alunos[i].append(media)
		else:
			alunos[i].append(0)

	return alunos

def add_situacao(alunos):
	for i in range(len(alunos)):
		if(alunos[i][1] == 'A'):
			if(alunos[i][4] < 4):
				situacao = 'REPROVADO'
			elif(alunos[i][4] >=4 and alunos[i][4] < 7):
				situacao = 'PROVA FINAL'
			elif(alunos[i][4] > 7):
				situacao = 'APROVADO'
		else:
			situacao = 'EVADIDO'

		alunos[i].append(situacao)

	return alunos



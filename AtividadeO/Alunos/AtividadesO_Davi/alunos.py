def main():
	#Entrada
	alunos = int(input('Insira o número de alunos: '))

	# Processamento
	cont = 1
	apro = 0
	repro = 0
	pf = 0
	soma_classe = 0
	print('Insira os dados da seguinte forma: nome n1 n2 n3')
	while cont <= alunos:
		entrada = input('Dados: ')
		nome, n1, n2, n3 = entrada.split(' ')
		n1 = float(n1)
		n2 = float(n2)
		n3 = float(n3)
		nota = (n1 + n2 + n3) / 3
		print("Aluno %s, nota final: %.2f" %(nome, nota))
		soma_classe += nota
		if nota >= 7:
			apro += 1
		elif nota >= 4 and nota < 7:
			pf += 1
		elif nota < 4:
			repro += 1
		cont += 1

	# Saída
	print('----------------------------')
	print('Media da Classe: %.2f' %(soma_classe / alunos))
	print('Aprovados: %d' %apro)
	print('Reprovados: %d' %repro)
	print('Prova final: %d' %pf)


if __name__ == '__main__':
	main()
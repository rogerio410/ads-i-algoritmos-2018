def main():
	#entrada
	n = int(input())
	media_classe = 0
	aprovados = 0
	reprovados = 0
	prova_final = 0
	
	#processamento
	for i in range(n):
		nome, n1, n2, n3 = input().split()
		n1 = int(n1)
		n2 = int(n2)
		n3 = int(n3)

		media_aluno = (n1 + n2 + n3) / 3

		media_classe += media_aluno

		if media_aluno >= 7:
			aprovados += 1
		elif media_aluno >= 4:
			prova_final += 1
		else:
			reprovados += 1
	
	media_classe = media_classe / n

	#saida
	print('Média da classe: %.2f' %media_classe)
	print('Quantidade de alunso aprovados: %d' %aprovados)
	print('Quantidade de alunos em prova final:', prova_final)
	print('Quantidade de alunos reprovados:',reprovados)


if __name__ == '__main__':
	main()
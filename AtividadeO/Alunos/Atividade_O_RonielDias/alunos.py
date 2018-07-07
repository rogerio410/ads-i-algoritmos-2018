def main():
	# entrada
	quant = int(input("Informe a quantidade de alunos\n>> "))
	aluno = list(range(quant))

	mediaClasse = 0
	nAprovados = 0
	nReprovados = 0
	nExameFinal = 0
	for i in range(quant):
		if(i != quant):
			print("------------------------------------------------------------")

		# entrada
		print("			ALUNO %d" % (i+1))
		n1 = float(input("Nota1: "))
		n2 = float(input("Nota2: "))
		n3 = float(input("Nota3: "))

		media = (n1+n2+n3) / 3
		print("\nMedia = %.2f" % (media))

		mediaClasse = mediaClasse + media

		if(media>=7):
			nAprovados = nAprovados + 1
			# saída
			print("Aluno aprovado")
		elif(media<7 and media>=4):
			nExameFinal = nExameFinal + 1
			# saída
			print("Aluno em exame final")
		elif(media<4):
			nReprovados = nReprovados + 1
			# saida
			print("Aluno reprovado")

	# saída
	print("------------------------------------------------------------")
	print("			RELATORIO FINAL")
	print("Numero de alunos Aprovados = %d" % nAprovados)
	print("Numero de alunos em Exame Final = %d" % nExameFinal)
	print("Numero de alunos Reprovados = %d" % nReprovados)
	print("Media da classe = %.1f" % (mediaClasse / quant))

if __name__ == '__main__':
	main()


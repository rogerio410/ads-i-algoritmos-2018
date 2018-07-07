def main():
	Aluno = int(input())
	Situação_Classe(Alunos)


def Situação_Classe(num):
	i = 0
	Media_Classe = 0
	Aprovados = 0
	Prova_Final = 0
	Reprovados = 0

	while i < num:
		Nome = input()
		Nota_1 = float(input())
		Nota_2 = float(input())
		Nota_3 = float(input())

		Media_Aluno = (Nota_1 + Nota_2 + Nota_3) / 3

		if Media_Aluno >= 7:
			Aprovados += 1
		elif 7 > Media_Aluno > 4:
		    Prova_Final	+= 1
		elif Media_Aluno < 4   
		    Reprovados += 1

		Media_Classe += Media_Aluno
		i = i + 1

	Media_Classe = Media_Classe / Media_Aluno
	print("Média Da Classe = %.2f" % Media_Classe)
	print("Quantidade De Alunos Aprovados: %d" % Aprovados)
	print("Quantidade De Alunos Reprovados: %d" % Reprovados)
	print("Quantidade De Alunos de Prova Final: %d" % Prova_Final)


	if __name__ == '__main__':
		main()
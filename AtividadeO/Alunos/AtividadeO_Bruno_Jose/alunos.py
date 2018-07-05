def main():
	numero_aluno = int(input())
	situacao_da_classe(numero_aluno)


def situacao_da_classe(num):
	i = 0
	aprovado = 0
	reprovado = 0
	prova_final = 0
	media_classe = 0

	while i < num:
		nome = input()
		nota_1 = float(input())
		nota_2 = float(input())
		nota_3 = float(input())

		media_aluno = (nota_1 + nota_2 + nota_3) / 3

		if media_aluno >= 7:
			aprovado += 1
		elif 7 > media_aluno > 4:
			prova_final += 1
		elif media_aluno < 4:
			reprovado += 1
		
		media_classe += media_aluno
		i = i + 1

	media_classe = media_classe / num

	print("Media da classe = %.2f" % media_classe)
	print("Quantidade de alunos aprovados: %d" % aprovado)
	print("Quantidade de alunos reprovados: %d" % reprovado)
	print("Quantidade de alunos de prova final: %d" % prova_final)


if __name__ == '__main__':
	main()
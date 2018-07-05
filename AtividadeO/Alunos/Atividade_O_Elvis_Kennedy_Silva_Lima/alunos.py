def main():

	numero_de_alunos = int(input())
	aprovados = 0
	reprovados = 0
	prova_final = 0
	media_da_classe = 0

	for i in range(1, numero_de_alunos + 1):
		entrada = input()
		partes = entrada.split()
		nome = str(partes[0])
		nota1 = float(partes[1])
		nota2 = float(partes[2])
		nota3 = float(partes[3])

		media_aritmetica = (nota1+nota2+nota3) / 3

		media_da_classe = (media_da_classe + media_aritmetica) / numero_de_alunos

		if media_aritmetica >= 7.0:
			aprovados = aprovados + 1
		elif media_aritmetica < 7.0 and media_aritmetica >= 4:
			reprovados = reprovados +1
		elif media_aritmetica < 4.0:
			prova_final = prova_final + 1

	print('Numero de aprovados:', aprovados)
	print('Numero de reprovados:', reprovados)
	print('Numero de alunos em prova final:', prova_final)

if __name__ == '__main__':
	main()
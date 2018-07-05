def main():
	numero = int(input())

	perfeito = eh_perfeito(numero)

	print("O Numero eh: ", perfeito)


def eh_perfeito(num):
	soma = 0
	for i in range(1, num):
		if num % i == 0:
			soma += i
	if num == soma:
		return "Perfeito"
	else:
		return "Nao Perfeito"



if __name__ == '__main__':
	main()
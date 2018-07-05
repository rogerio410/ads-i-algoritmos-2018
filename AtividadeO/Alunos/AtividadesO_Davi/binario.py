def main():
	
	# Entrada
	n = input('Insira um numero: ')

	# Processamento
	multi = 1
	i = len(n)
	cont = 1
	soma = 0
	while cont <= len(n):
		soma += int(n[i - 1]) * multi
		i = i - 1
		multi = multi * 2
		cont = cont + 1

	# Saída
	print("O número binário '{}' em decimal é: '{}'.".format(n, soma))

if __name__ == '__main__':
	main()
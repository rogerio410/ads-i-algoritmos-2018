def main():

	# Entrada
	n = int(input('Insira um número: '))

	# Processamento
	soma = 0
	indice = 1
	while indice < n:
		
		if n % indice == 0:
			soma += indice
		
		indice += 1
	# Saída
	if n == soma:
		print('%d é perfeito.' %n)
	
	else:
		print('%d não é perfeito.' %n)

if __name__ == '__main__':
	main()
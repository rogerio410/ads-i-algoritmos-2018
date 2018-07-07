def main():
	#Entrada
	num = input('Insira um numero natural de 4 digítos: ')

	# Processamento
	n1 = num[0] + num[1]
	n1 = int(n1)
	n2 = num[2] + num[3]
	n2 = int(n2)
	n3 = n1 + n2

	# Saída
	if n3 * n3 == num:
		print('Raiz de %d é %d, que é a soma de %d com %d.' %(num,n3,n1,n2))

if __name__ == '__main__':
	main()
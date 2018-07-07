def main():
	# entrada
	n = int(input())

	# processamento
	soma = 0
	cont = 1
	while(cont<n):
		if(n%cont == 0):
			soma = soma+cont

		cont = cont+1

	if(n == soma):
		# saída1
		print("É um inteiro perfeito")
	else:
		# saída2
		print("Não é um inteiro perfeito")
		
if __name__ == '__main__':
	main()


	#OK
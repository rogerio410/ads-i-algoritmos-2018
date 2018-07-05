def main():

	# Entrada
	n1 = int(input('Insira o numero 1: '))
	n2 = int(input('Insira o numero 2: '))
	
	# Processamento
	aux = 0
	mdc = 0
	while True:
		try:
			aux = n1 % n2
			n1 = n2
			n2 = aux
			if aux > 0:
				mdc = aux
		except ZeroDivisionError:
			break
	# Saída
	print('O máximo divisor comum é', mdc)

if __name__ == '__main__':
		main()
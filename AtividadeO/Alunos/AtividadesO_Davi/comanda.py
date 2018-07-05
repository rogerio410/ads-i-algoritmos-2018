import os



def main():
	total = 0
	
	while True:
		print('1 - Inserir produtos.\n2 - Definir quantidade de pagantes na mesa:\n3 - Imprimir Conta\n4 - Confirmar pagamento.')
		op = input('Insira a opção: ')

		if op == '1':
			# INSERIR PRODUTOS
			while True:
				entrada = input("Digite a quantidade e 1 produto por linha ou digite 0 para voltar.\nEx: '1 A', na linha seguinte '2 T'\n")
				if entrada != '0':
					if entrada[2] == 'C':
						valor = float(entrada[0] * 8)
						total += valor 
					elif entrada[2] == 'T':
						valor = float(entrada[0] * 29)
						total += valor 
					elif entrada[2] == 'A':
						valor = float(entrada[0] * 2)
						total += valor
				else:
					break
			# / INSERIR PRODUTOS
		elif op == '2':
			# QUANTIDADE DE PAGANTES
			pagantes = int(input('Insira a quantidade de pagantes: '))
			# / QUANTIDADE DE PAGANTES
		elif op == '3':
			tax = (total / 100) * 10
			print('Valor da conta: %.2f' %total)
			print('Valor da taxa: %.2f' %(tax))
			print('Valor total com taxa: %.2f' %(total + tax))
			print('Valor por pagante: %.2f' %(total / pagantes))
		elif op == '4':
			total = 0
		print(total)

if __name__ == '__main__':
	main()
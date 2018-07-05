def main():
	conta = 0
	n = 1
	taxa = 0
	while True:
		menu = '\n\n########### MENU ###########\n'\
			   'A - inserir produtos\n'\
			   'B - definir a quantidade de pagantes\n'\
			   'C - calcular a conta, incluindo os 10%% da taxa de serviço\n'\
			   'D - imprimir conta\n'\
			   'E - confirmar pagamento que zera conta da mesa'\
			   'F - sair'
		print(menu)
		
		opçao = input().lower()

		if opçao == 'a':
			produto = inserir_produto()
			conta += produto
		
		elif opçao == 'b':
			n = int(input('Qual a quantidade de pagantes?\n'))
		
		elif opçao == 'c':
			taxa = conta * 0.10	
		
		elif opçao == 'd':
			print('Valor da conta: %.2f R$'%conta)
			print('Valor da taxa: %.2f R$' %taxa)
			print('Valor total com taxa de serviço: %.2f R$' %(conta + taxa))
			print('Valor por pagantes: %.2f R$' %((conta + taxa)/n))
		
		elif opçao == 'e':
			conta = 0
			n = 1
			taxa = 0
		
		elif opçao == 'f':
			break


def inserir_produto():
	cerveja = 8
	tira_gosto = 29
	agua = 2
	valor = 0

	qnt, produto = input().split()
	qnt = int(qnt)
	if produto.lower() == 'c':
		valor = qnt * cerveja
	elif produto.lower() == 't':
		valor = qnt * tira_gosto
	elif produto.lower() == 'a':
		valor = qnt * agua
	
	return valor

if __name__ == '__main__':
	main()
import os

quantPagantes = 1
somaConta = 0

def main():
	resp = -1
	while (resp!=0):

		os.system("cls")
		resp = menu()

		if(resp == 1):
			inserir_produto()
		elif(resp == 2):
			quant_pagantes()
		elif(resp == 3):
			imprimir_conta()
		elif(resp == 4):
			confirmar_pagamento()


def menu():
	print("------------------------------------------------------------")
	print("			MENU")
	print("------------------------------------------------------------")
	print("1. Inserir produto")
	print("2. Definir quantidade de pagantes")
	print("3. Imprimir conta")
	print("4. Confirmar pagamento")
	print("0. Encerrar")
	print("------------------------------------------------------------")
	resp = int(input("Escolha uma opcao: "))

	return resp

def inserir_produto():
	global somaConta
	
	os.system("cls")
	print("------------------------------------------------------------")
	print("			INSERIR PRODUTO")
	print("------------------------------------------------------------")
	numero, letra = input("Informe a quantidade(NUMERO) e o codigo do produto(LETRA MAUISCULA)\n>> ").split(" ")
	numero = int(numero)

	if(letra == 'C'):
		print("%d cerveja(s) inserida(s)!" % numero)
		somaConta = somaConta + (numero*8)
	elif(letra == 'T'):
		print("%d tira-gosto(s) inserido(s)!" % numero)
		somaConta = somaConta + (numero*29)
	elif(letra == 'A'):
		print("%d agua(s) inserida(s)" % numero)
		somaConta = somaConta + (numero*2)

	input("\nDigite uma tecla para continuar...")


def quant_pagantes():
	global quantPagantes
	
	os.system("cls")
	print("------------------------------------------------------------")
	print("			QUANTIDADE DE PAGANTES")
	print("------------------------------------------------------------")
	qPagantes = int(input("Informe a quantidade de pagantes\n>> "))

	quantPagantes = qPagantes
	input("\nDigite uma tecla para continuar...")


def imprimir_conta():
	global somaConta
	global quantPagantes

	os.system("cls")
	print("------------------------------------------------------------")
	print("			IMPRIMIR CONTA")
	print("------------------------------------------------------------")
	valorConta = somaConta
	valorTaxa = valorConta * 0.10
	valorTotal = valorConta + valorTaxa
	valorPagante = valorTotal / quantPagantes

	print("Valor da conta: R$ %.2f" % valorConta)
	print("Valor da taxa de serviço: R$ %.2f" % valorTaxa)
	print("Valor Total com taxa de serviço: R$ %.2f" % valorTotal)
	print("Valor por pagante: R$ %.2f" % valorPagante)

	input("\nDigite uma tecla para continuar...")

def confirmar_pagamento():
	global somaConta
	global quantPagantes

	os.system("cls")
	print("------------------------------------------------------------")
	print("			IMPRIMIR CONTA")
	print("------------------------------------------------------------")
	print("Pagamento realizado!")
	input("\nDigite uma tecla para continuar...")

	somaConta = 0
	quantPagantes = 0

if __name__ == '__main__':
	main()

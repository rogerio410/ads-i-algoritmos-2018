def main():
	
	opc1 = adição_da_esquerda_para_direita()
	opc2 = adição_da_direita_para_esquerda()
	opc3 = separação_dos_termos_positivos_e_negativos_da_Esquerda_p_Direita()
	opc4 = separação_dos_termos_positivos_e_negativos_da_Direita_p_Esquerda()

	if opc1 == opc2 == opc3 == opc4:
		print('Todas são iguais')


def adição_da_esquerda_para_direita():
	somador = 0
	for i in range(1,10001):
		if i % 2 != 0:
			somador += 1/i
		else:
			somador -= 1/i

	print('Soma da esquerda para direita: %.2f' %somador)

	return round(somador,2)


def adição_da_direita_para_esquerda():
	somador = 0
	for i in range(10000, 0, -1):
		if i % 2 == 0:
			somador -= 1/i 
		else:
			somador += 1/i 

	print('Soma da direita para a esquerda: %.2f' %somador)

	return round(somador,2)


def separação_dos_termos_positivos_e_negativos_da_Esquerda_p_Direita():
	soma_positivo = 0
	soma_negativo = 0
	for i in range(1, 10001):
		if i % 2 != 0:
			soma_positivo += 1/i
		else:
			soma_negativo -= 1/i
	print('Soma dos positivos da E -> D: %.2f' %soma_positivo)
	print('Soma dos negativos da E -> D: %.2f' %soma_negativo)

	somador = soma_positivo + soma_negativo
	
	return round(somador,2)


def separação_dos_termos_positivos_e_negativos_da_Direita_p_Esquerda():
	soma_positivo = 0
	soma_negativo = 0
	for i in range(10000, 0, -1):
		if i % 2 == 0:
			soma_negativo -= 1/i
		else:
			soma_positivo += 1/i

	print('Soma dos positivos da D -> E: %.2f' %soma_positivo)
	print('Soma dos negativos da D -> E: %.2f' %soma_negativo)

	somador = soma_positivo + soma_negativo
	
	return round(somador,2)

if __name__ == '__main__':
	main()
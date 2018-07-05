def main():

	numero_binario = (input('Digite um numero na base binária: '))
	posicao = 0
	numero_em_decimal = 0
	for i in numero_binario:
		numero_em_decimal = numero_em_decimal + int(i) * (2 ** posicao-1)
		posicao = posicao + 1
	
	print(numero_em_decimal)

if __name__ == '__main__':
	main()
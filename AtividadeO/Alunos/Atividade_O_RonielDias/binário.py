import math

def main():
	# entrada
	binario = input("Digite um numero binario>> ")

	# processamento
	aux = binario[::-1]  # NAO PERMITIDO

	tam = len(aux)

	soma = 0
	for i in range(tam):
		if(aux[i] == '1'):
			num = 1
		elif(aux[i] == '0'):
			num = 0

		soma = soma + (num*pow(i, 2))

	# saída
	print(soma)

if __name__ == '__main__':
	main()